from database_connection import conectar

def criar_reserva(id_usuario, id_exemplar, data_reserva):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Reservas (id_usuario, id_exemplar, data_reserva) VALUES (%s, %s, %s)"
        valores = (id_usuario, id_exemplar, data_reserva)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Reserva criada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar reserva: {err}")
    finally:
        cursor.close()
        conexao.close()

def listar_reservas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Reservas")
        reservas = cursor.fetchall()
        return reservas
    except mysql.connector.Error as err:
        print(f"Erro ao listar reservas: {err}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_reserva(id_reserva, id_usuario, id_exemplar, data_reserva):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Reservas SET id_usuario = %s, id_exemplar = %s, data_reserva = %s WHERE id_reserva = %s"
        valores = (id_usuario, id_exemplar, data_reserva, id_reserva)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Reserva atualizada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar reserva: {err}")
    finally:
        cursor.close()
        conexao.close()

def deletar_reserva(id_reserva):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM Reservas WHERE id_reserva = %s"
        valores = (id_reserva,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Reserva deletada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao deletar reserva: {err}")
    finally:
        cursor.close()
        conexao.close()