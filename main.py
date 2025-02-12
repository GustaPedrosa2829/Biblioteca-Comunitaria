from crud_usuarios import criar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario
from crud_obras import criar_obra, listar_obras, atualizar_obra, deletar_obra
from crud_autores import criar_autor, listar_autores, atualizar_autor, deletar_autor
from crud_exemplares import criar_exemplar, listar_exemplares, atualizar_exemplar, deletar_exemplar
from crud_emprestimos import criar_emprestimo, listar_emprestimos, atualizar_emprestimo, deletar_emprestimo
from crud_reservas import criar_reserva, listar_reservas, atualizar_reserva, deletar_reserva

def menu_usuarios():
    while True:
        print("\n--- Menu de Usuários ---")
        print("1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            status = input("Status (aluno/professor/funcionario): ")
            criar_usuario(nome, endereco, telefone, status)

        elif opcao == "2":
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(usuario)

        elif opcao == "3":
            id_usuario = input("ID do Usuário: ")
            nome = input("Novo Nome: ")
            endereco = input("Novo Endereço: ")
            telefone = input("Novo Telefone: ")
            status = input("Novo Status (aluno/professor/funcionario): ")
            atualizar_usuario(id_usuario, nome, endereco, telefone, status)

        elif opcao == "4":
            id_usuario = input("ID do Usuário: ")
            deletar_usuario(id_usuario)

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_obras():
    while True:
        print("\n--- Menu de Obras ---")
        print("1. Criar Obra")
        print("2. Listar Obras")
        print("3. Atualizar Obra")
        print("4. Deletar Obra")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            ano_publicacao = input("Ano de Publicação: ")
            edicao = input("Edição: ")
            id_editora = input("ID da Editora: ")
            criar_obra(titulo, ano_publicacao, edicao, id_editora)

        elif opcao == "2":
            obras = listar_obras()
            for obra in obras:
                print(obra)

        elif opcao == "3":
            id_obra = input("ID da Obra: ")
            titulo = input("Novo Título: ")
            ano_publicacao = input("Novo Ano de Publicação: ")
            edicao = input("Nova Edição: ")
            id_editora = input("Novo ID da Editora: ")
            atualizar_obra(id_obra, titulo, ano_publicacao, edicao, id_editora)

        elif opcao == "4":
            id_obra = input("ID da Obra: ")
            deletar_obra(id_obra)

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_autores():
    while True:
        print("\n--- Menu de Autores ---")
        print("1. Criar Autor")
        print("2. Listar Autores")
        print("3. Atualizar Autor")
        print("4. Deletar Autor")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_autor = input("Nome do Autor: ")
            criar_autor(nome_autor)

        elif opcao == "2":
            autores = listar_autores()
            for autor in autores:
                print(autor)

        elif opcao == "3":
            id_autor = input("ID do Autor: ")
            nome_autor = input("Novo Nome do Autor: ")
            atualizar_autor(id_autor, nome_autor)

        elif opcao == "4":
            id_autor = input("ID do Autor: ")
            deletar_autor(id_autor)

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_exemplares():
    while True:
        print("\n--- Menu de Exemplares ---")
        print("1. Criar Exemplar")
        print("2. Listar Exemplares")
        print("3. Atualizar Exemplar")
        print("4. Deletar Exemplar")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_obra = input("ID da Obra: ")
            status = input("Status (disponível/emprestado): ")
            criar_exemplar(id_obra, status)

        elif opcao == "2":
            exemplares = listar_exemplares()
            for exemplar in exemplares:
                print(exemplar)

        elif opcao == "3":
            id_exemplar = input("ID do Exemplar: ")
            id_obra = input("Novo ID da Obra: ")
            status = input("Novo Status (disponível/emprestado): ")
            atualizar_exemplar(id_exemplar, id_obra, status)

        elif opcao == "4":
            id_exemplar = input("ID do Exemplar: ")
            deletar_exemplar(id_exemplar)

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_emprestimos():
    while True:
        print("\n--- Menu de Empréstimos ---")
        print("1. Criar Empréstimo")
        print("2. Listar Empréstimos")
        print("3. Atualizar Empréstimo")
        print("4. Deletar Empréstimo")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_usuario = input("ID do Usuário: ")
            id_exemplar = input("ID do Exemplar: ")
            data_emprestimo = input("Data de Empréstimo (AAAA-MM-DD): ")
            data_devolucao_prevista = input("Data de Devolução Prevista (AAAA-MM-DD): ")
            criar_emprestimo(id_usuario, id_exemplar, data_emprestimo, data_devolucao_prevista)

        elif opcao == "2":
            emprestimos = listar_emprestimos()
            for emprestimo in emprestimos:
                print(emprestimo)

        elif opcao == "3":
            id_emprestimo = input("ID do Empréstimo: ")
            data_devolucao_real = input("Nova Data de Devolução Real (AAAA-MM-DD): ")
            atualizar_emprestimo(id_emprestimo, data_devolucao_real)

        elif opcao == "4":
            id_emprestimo = input("ID do Empréstimo: ")
            deletar_emprestimo(id_emprestimo)

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_reservas():
    while True:
        print("\n--- Menu de Reservas ---")
        print("1. Criar Reserva")
        print("2. Listar Reservas")
        print("3. Atualizar Reserva")
        print("4. Deletar Reserva")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_usuario = input("ID do Usuário: ")
            id_exemplar = input("ID do Exemplar: ")
            data_reserva = input("Data da Reserva (AAAA-MM-DD): ")
            criar_reserva(id_usuario, id_exemplar, data_reserva)

        elif opcao == "2":
            reservas = listar_reservas()
            for reserva in reservas:
                print(reserva)

        elif opcao == "3":
            id_reserva = input("ID da Reserva: ")
            id_usuario = input("Novo ID do Usuário: ")
            id_exemplar = input("Novo ID do Exemplar: ")
            data_reserva = input("Nova Data da Reserva (AAAA-MM-DD): ")
            atualizar_reserva(id_reserva, id_usuario, id_exemplar, data_reserva)

        elif opcao == "4":
            id_reserva = input("ID da Reserva: ")
            deletar_reserva(id_reserva)

        elif opcao == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n--- Sistema de Biblioteca Universitária ---")
        print("1. Usuários")
        print("2. Obras")
        print("3. Autores")
        print("4. Exemplares")
        print("5. Empréstimos")
        print("6. Reservas")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_usuarios()
        elif opcao == "2":
            menu_obras()
        elif opcao == "3":
            menu_autores()
        elif opcao == "4":
            menu_exemplares()
        elif opcao == "5":
            menu_emprestimos()
        elif opcao == "6":
            menu_reservas()
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()