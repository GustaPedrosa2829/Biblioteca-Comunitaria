from database_connection import conectar

def criar_emprestimo(id_usuario, id_exemplar, data_emprestimo, data_devolucao_prevista):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Emprestimos (id_usuario, id_exemplar, data_emprestimo, data_devolucao_prevista) VALUES (%s, %s, %s, %s)"
        valores = (id_usuario, id_exemplar, data_emprestimo, data_devolucao_prevista)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Empréstimo criado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar empréstimo: {err}")
    finally:
        cursor.close()
        conexao.close()

def listar_emprestimos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Emprestimos")
        emprestimos = cursor.fetchall()
        return emprestimos
    except mysql.connector.Error as err:
        print(f"Erro ao listar empréstimos: {err}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_emprestimo(id_emprestimo, data_devolucao_real):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Emprestimos SET data_devolucao_real = %s WHERE id_emprestimo = %s"
        valores = (data_devolucao_real, id_emprestimo)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Empréstimo atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar empréstimo: {err}")
    finally:
        cursor.close()
        conexao.close()

def deletar_emprestimo(id_emprestimo):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM Emprestimos WHERE id_emprestimo = %s"
        valores = (id_emprestimo,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Empréstimo deletado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao deletar empréstimo: {err}")
    finally:
        cursor.close()
        conexao.close()