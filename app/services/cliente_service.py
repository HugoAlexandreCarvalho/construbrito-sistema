from app.database.db import get_connection

def cadastrar_cliente(nome, telefone):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO clientes (nome, telefone) VALUES (%s, %s)"
    valores = (nome, telefone)

    cursor.execute(sql, valores)
    conn.commit()

    print("Cliente cadastrado com sucesso!")

    cursor.close()
    conn.close()


def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    cursor.close()
    conn.close()

def buscar_cliente_por_nome(nome):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT id, nome FROM clientes WHERE nome LIKE %s"
    cursor.execute(sql, (f"%{nome}%",))

    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultados



from datetime import datetime, timedelta
from app.database.db import get_connection


def verificar_inadimplencia():
    conn = get_connection()
    cursor = conn.cursor()

    # Pega vendas com mais de 30 dias
    sql = """
        SELECT cliente_id
        FROM vendas
        WHERE data_venda < NOW() - INTERVAL 30 DAY
    """

    cursor.execute(sql)
    resultados = cursor.fetchall()

    clientes_inadimplentes = set([r[0] for r in resultados])

    # Bloquear clientes
    for cliente_id in clientes_inadimplentes:
        cursor.execute(
            "UPDATE clientes SET status = 'bloqueado' WHERE id = %s",
            (cliente_id,)
        )

    conn.commit()

    cursor.close()
    conn.close()