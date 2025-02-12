import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="seu_usuario",
            password="sua_senha",
            database="biblioteca_universitaria"
        )
        print("Conexão ao banco de dados realizada com sucesso!")
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None