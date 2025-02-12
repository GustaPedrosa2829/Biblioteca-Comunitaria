from database_connection import conectar

def criar_exemplar(id_obra, status):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Exemplares (id_obra, status) VALUES (%s, %s)"
        valores = (id_obra, status)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Exemplar criado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar exemplar: {err}")
    finally:
        cursor.close()
        conexao.close()

def listar_exemplares():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Exemplares")
        exemplares = cursor.fetchall()
        return exemplares
    except mysql.connector.Error as err:
        print(f"Erro ao listar exemplares: {err}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_exemplar(id_exemplar, id_obra, status):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Exemplares SET id_obra = %s, status = %s WHERE id_exemplar = %s"
        valores = (id_obra, status, id_exemplar)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Exemplar atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar exemplar: {err}")
    finally:
        cursor.close()
        conexao.close()

def deletar_exemplar(id_exemplar):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM Exemplares WHERE id_exemplar = %s"
        valores = (id_exemplar,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Exemplar deletado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao deletar exemplar: {err}")
    finally:
        cursor.close()
        conexao.close()