import mysql.connector
from mysql.connector import Error

def criar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="adm",
            password="123456789"
        )
        
        if conexao.is_connected():
            cursor = conexao.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca_universitaria")
            print("Banco de dados criado com sucesso!")
            
            cursor.execute("USE biblioteca_universitaria")
            
            tabelas = {
                'Usuarios': """
                CREATE TABLE IF NOT EXISTS Usuarios (
                    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100),
                    endereco VARCHAR(200),
                    telefone VARCHAR(20),
                    status ENUM('aluno', 'professor', 'funcionario')
                )""",
                
                'Editoras': """
                CREATE TABLE IF NOT EXISTS Editoras (
                    id_editora INT AUTO_INCREMENT PRIMARY KEY,
                    nome_editora VARCHAR(100)
                )""",
                
                'Obras': """
                CREATE TABLE IF NOT EXISTS Obras (
                    id_obra INT AUTO_INCREMENT PRIMARY KEY,
                    titulo VARCHAR(150),
                    ano_publicacao INT,
                    edicao INT,
                    id_editora INT,
                    FOREIGN KEY (id_editora) REFERENCES Editoras(id_editora)
                )""",
                
                'Autores': """
                CREATE TABLE IF NOT EXISTS Autores (
                    id_autor INT AUTO_INCREMENT PRIMARY KEY,
                    nome_autor VARCHAR(100)
                )""",
                
                'Obras_Autores': """
                CREATE TABLE IF NOT EXISTS Obras_Autores (
                    id_obra INT,
                    id_autor INT,
                    PRIMARY KEY (id_obra, id_autor),
                    FOREIGN KEY (id_obra) REFERENCES Obras(id_obra),
                    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor)
                )""",
                
                'Exemplares': """
                CREATE TABLE IF NOT EXISTS Exemplares (
                    id_exemplar INT AUTO_INCREMENT PRIMARY KEY,
                    id_obra INT,
                    status ENUM('disponível', 'emprestado'),
                    FOREIGN KEY (id_obra) REFERENCES Obras(id_obra)
                )""",
                
                'Emprestimos': """
                CREATE TABLE IF NOT EXISTS Emprestimos (
                    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
                    id_usuario INT,
                    id_exemplar INT,
                    data_emprestimo DATE,
                    data_devolucao_prevista DATE,
                    data_devolucao_real DATE,
                    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
                    FOREIGN KEY (id_exemplar) REFERENCES Exemplares(id_exemplar)
                )""",
                
                'Reservas': """
                CREATE TABLE IF NOT EXISTS Reservas (
                    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
                    id_usuario INT,
                    id_exemplar INT,
                    data_reserva DATE,
                    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
                    FOREIGN KEY (id_exemplar) REFERENCES Exemplares(id_exemplar)
                )"""
            }
            
            for nome_tabela, ddl in tabelas.items():
                try:
                    print(f"Criando tabela {nome_tabela}...")
                    cursor.execute(ddl)
                    print(f"Tabela {nome_tabela} criada com sucesso!")
                except Error as err:
                    print(f"Erro ao criar tabela {nome_tabela}: {err}")
            
    except Error as err:
        print(f"Erro: {err}")
        
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão ao MySQL fechada")

if __name__ == "__main__":
    criar_banco()