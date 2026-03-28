from app.database.db import get_connection


def registrar_venda(cliente_id, itens):
    conn = get_connection()
    cursor = conn.cursor()

    # Verificar cliente
    cursor.execute("SELECT status FROM clientes WHERE id = %s", (cliente_id,))
    status = cursor.fetchone()

    if status and status[0] == "bloqueado":
        print("Cliente bloqueado! Venda não permitida.")
        return

    total = 0

    # Calcular total
    for item in itens:
        produto_id, quantidade = item

        cursor.execute("SELECT preco, estoque FROM produtos WHERE id = %s", (produto_id,))
        produto = cursor.fetchone()

        if not produto:
            print(f"Produto {produto_id} não encontrado!")
            return

        preco, estoque = produto

        if estoque < quantidade:
            print(f"Estoque insuficiente para produto {produto_id}")
            return

        total += preco * quantidade

    # Criar venda
    cursor.execute(
        "INSERT INTO vendas (cliente_id, total) VALUES (%s, %s)",
        (cliente_id, total)
    )
    venda_id = cursor.lastrowid

    # Inserir itens + atualizar estoque
    for item in itens:
        produto_id, quantidade = item

        cursor.execute("SELECT preco FROM produtos WHERE id = %s", (produto_id,))
        preco = cursor.fetchone()[0]

        cursor.execute(
            "INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)",
            (venda_id, produto_id, quantidade, preco)
        )

        cursor.execute(
            "UPDATE produtos SET estoque = estoque - %s WHERE id = %s",
            (quantidade, produto_id)
        )

    conn.commit()

    print(f"Venda registrada! Total: R$ {total:.2f}")

    cursor.close()
    conn.close()