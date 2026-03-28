from app.services.cliente_service import (
    cadastrar_cliente,
    listar_clientes,
    buscar_cliente_por_nome,
    verificar_inadimplencia
)

from app.services.produto_service import (
    cadastrar_produto,
    listar_produtos
)

from app.services.venda_service import registrar_venda


def menu():
    while True:
        # 🔒 Verifica inadimplência automaticamente
        verificar_inadimplencia()

        print("\n--- SISTEMA CONSTRUBRITO ---")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Registrar Venda")
        print("4 - Cadastrar Produto")
        print("5 - Listar Produtos")
        print("0 - Sair")

        opcao = input("Escolha: ")

        # =========================
        # CADASTRAR CLIENTE
        # =========================
        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            cadastrar_cliente(nome, telefone)

        # =========================
        # LISTAR CLIENTES
        # =========================
        elif opcao == "2":
            listar_clientes()

        # =========================
        # REGISTRAR VENDA COMPLETA
        # =========================
        elif opcao == "3":
            nome = input("Nome do cliente: ")

            resultados = buscar_cliente_por_nome(nome)

            if not resultados:
                print("Cliente não encontrado!")
                continue

            print("\nClientes encontrados:")
            for cliente in resultados:
                print(f"ID: {cliente[0]} | Nome: {cliente[1]}")

            try:
                cliente_id = int(input("Digite o ID do cliente: "))
            except ValueError:
                print("Digite um número válido!")
                continue

            # Mostrar produtos
            print("\n--- PRODUTOS DISPONÍVEIS ---")
            listar_produtos()

            itens = []

            while True:
                produto_id = input("\nID do produto (ou 0 para finalizar): ")

                if produto_id == "0":
                    break

                try:
                    produto_id = int(produto_id)
                    quantidade = int(input("Quantidade: "))
                except ValueError:
                    print("Digite valores válidos!")
                    continue

                itens.append((produto_id, quantidade))

            if not itens:
                print("Nenhum item adicionado!")
                continue

            registrar_venda(cliente_id, itens)

        # =========================
        # CADASTRAR PRODUTO
        # =========================
        elif opcao == "4":
            nome = input("Nome do produto: ")

            try:
                preco = float(input("Preço: "))
                estoque = int(input("Estoque: "))
            except ValueError:
                print("Digite valores válidos!")
                continue

            cadastrar_produto(nome, preco, estoque)

        # =========================
        # LISTAR PRODUTOS
        # =========================
        elif opcao == "5":
            listar_produtos()

        # =========================
        # SAIR
        # =========================
        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()