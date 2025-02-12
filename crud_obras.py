from database_connection import conectar

def criar_obra(titulo, ano_publicacao, edicao, id_editora):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Obras (titulo, ano_publicacao, edicao, id_editora) VALUES (%s, %s, %s, %s)"
        valores = (titulo, ano_publicacao, edicao, id_editora)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Obra criada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar obra: {err}")
    finally:
        cursor.close()
        conexao.close()

def listar_obras():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Obras")
        obras = cursor.fetchall()
        return obras
    except mysql.connector.Error as err:
        print(f"Erro ao listar obras: {err}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_obra(id_obra, titulo, ano_publicacao, edicao, id_editora):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Obras SET titulo = %s, ano_publicacao = %s, edicao = %s, id_editora = %s WHERE id_obra = %s"
        valores = (titulo, ano_publicacao, edicao, id_editora, id_obra)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Obra atualizada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar obra: {err}")
    finally:
        cursor.close()
        conexao.close()

def deletar_obra(id_obra):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM Obras WHERE id_obra = %s"
        valores = (id_obra,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Obra deletada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao deletar obra: {err}")
    finally:
        cursor.close()
        conexao.close()