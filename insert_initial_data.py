from database_connection import conectar
from datetime import datetime, timedelta

def inserir_dados_iniciais():
    conexao = conectar()
    cursor = conexao.cursor()
    
    try:
        # Inserir editoras
        editoras = [
            "Companhia das Letras",
            "Pearson",
            "McGraw Hill",
            "Atlas",
            "Bookman"
        ]
        
        for editora in editoras:
            cursor.execute(
                "INSERT INTO Editoras (nome_editora) VALUES (%s)",
                (editora,)
            )
        
        # Inserir autores
        autores = [
            "José Saramago",
            "Machado de Assis",
            "Thomas H. Cormen",
            "Robert C. Martin",
            "Donald Knuth"
        ]
        
        for autor in autores:
            cursor.execute(
                "INSERT INTO Autores (nome_autor) VALUES (%s)",
                (autor,)
            )
        
        # Inserir obras
        obras = [
            ("Ensaio sobre a Cegueira", 1995, 1, 1),
            ("Dom Casmurro", 1899, 1, 1),
            ("Introduction to Algorithms", 2009, 3, 2),
            ("Clean Code", 2008, 1, 3),
            ("The Art of Computer Programming", 1968, 1, 3)
        ]
        
        for obra in obras:
            cursor.execute(
                "INSERT INTO Obras (titulo, ano_publicacao, edicao, id_editora) VALUES (%s, %s, %s, %s)",
                obra
            )
        
        # Relacionar obras e autores
        for i in range(1, 6):
            cursor.execute(
                "INSERT INTO Obras_Autores (id_obra, id_autor) VALUES (%s, %s)",
                (i, i)
            )
        
        # Inserir exemplares
        for id_obra in range(1, 6):
            # Inserir 3 exemplares para cada obra
            for _ in range(3):
                cursor.execute(
                    "INSERT INTO Exemplares (id_obra, status) VALUES (%s, 'disponível')",
                    (id_obra,)
                )
        
        # Inserir usuários
        usuarios = [
            ("João Silva", "Rua A, 123", "11999999999", "aluno"),
            ("Maria Santos", "Rua B, 456", "11988888888", "professor"),
            ("Pedro Souza", "Rua C, 789", "11977777777", "aluno"),
            ("Ana Oliveira", "Rua D, 321", "11966666666", "funcionario"),
            ("Carlos Lima", "Rua E, 654", "11955555555", "professor")
        ]
        
        for usuario in usuarios:
            cursor.execute(
                "INSERT INTO Usuarios (nome, endereco, telefone, status) VALUES (%s, %s, %s, %s)",
                usuario
            )
        
        # Inserir alguns empréstimos
        data_atual = datetime.now()
        emprestimos = [
            (1, 1, data_atual - timedelta(days=15), data_atual + timedelta(days=15), None),
            (2, 4, data_atual - timedelta(days=30), data_atual - timedelta(days=5), data_atual - timedelta(days=3)),
            (3, 7, data_atual - timedelta(days=10), data_atual + timedelta(days=20), None),
            (4, 10, data_atual - timedelta(days=45), data_atual - timedelta(days=15), data_atual - timedelta(days=20)),
            (5, 13, data_atual - timedelta(days=5), data_atual + timedelta(days=25), None)
        ]
        
        for emprestimo in emprestimos:
            cursor.execute(
                """INSERT INTO Emprestimos 
                   (id_usuario, id_exemplar, data_emprestimo, data_devolucao_prevista, data_devolucao_real) 
                   VALUES (%s, %s, %s, %s, %s)""",
                emprestimo
            )
            
            # Atualizar status do exemplar para 'emprestado' se ainda não foi devolvido
            if emprestimo[4] is None:
                cursor.execute(
                    "UPDATE Exemplares SET status = 'emprestado' WHERE id_exemplar = %s",
                    (emprestimo[1],)
                )
        
        # Inserir algumas reservas
        reservas = [
            (2, 2, data_atual - timedelta(days=5)),
            (3, 5, data_atual - timedelta(days=3)),
            (4, 8, data_atual - timedelta(days=1))
        ]
        
        for reserva in reservas:
            cursor.execute(
                "INSERT INTO Reservas (id_usuario, id_exemplar, data_reserva) VALUES (%s, %s, %s)",
                reserva
            )
        
        conexao.commit()
        print("Dados iniciais inseridos com sucesso!")
        
    except Exception as e:
        print(f"Erro ao inserir dados iniciais: {e}")
        conexao.rollback()
        
    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    inserir_dados_iniciais()