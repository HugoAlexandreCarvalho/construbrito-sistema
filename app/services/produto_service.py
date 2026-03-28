from app.database.db import get_connection


def cadastrar_produto(nome, preco, estoque):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, preco, estoque))

    conn.commit()
    print("Produto cadastrado com sucesso!")

    cursor.close()
    conn.close()


def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    for p in produtos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Preço: {p[2]} | Estoque: {p[3]}")

    cursor.close()
    conn.close()