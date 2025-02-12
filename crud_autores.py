from database_connection import conectar

def criar_autor(nome_autor):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Autores (nome_autor) VALUES (%s)"
        valores = (nome_autor,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Autor criado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar autor: {err}")
    finally:
        cursor.close()
        conexao.close()

def listar_autores():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Autores")
        autores = cursor.fetchall()
        return autores
    except mysql.connector.Error as err:
        print(f"Erro ao listar autores: {err}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_autor(id_autor, nome_autor):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Autores SET nome_autor = %s WHERE id_autor = %s"
        valores = (nome_autor, id_autor)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Autor atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar autor: {err}")
    finally:
        cursor.close()
        conexao.close()

def deletar_autor(id_autor):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM Autores WHERE id_autor = %s"
        valores = (id_autor,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Autor deletado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao deletar autor: {err}")
    finally:
        cursor.close()
        conexao.close()