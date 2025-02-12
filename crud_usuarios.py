from database_connection import conectar

def criar_usuario(nome, endereco, telefone, status):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Usuarios (nome, endereco, telefone, status) VALUES (%s, %s, %s, %s)"
        valores = (nome, endereco, telefone, status)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Usuário criado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao criar usuário: {err}")
    finally:
        cursor.close()
        conexao.close()

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Usuarios")
        usuarios = cursor.fetchall()
        return usuarios
    except mysql.connector.Error as err:
        print(f"Erro ao listar usuários: {err}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_usuario(id_usuario, nome, endereco, telefone, status):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "UPDATE Usuarios SET nome = %s, endereco = %s, telefone = %s, status = %s WHERE id_usuario = %s"
        valores = (nome, endereco, telefone, status, id_usuario)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Usuário atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar usuário: {err}")
    finally:
        cursor.close()
        conexao.close()

def deletar_usuario(id_usuario):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = "DELETE FROM Usuarios WHERE id_usuario = %s"
        valores = (id_usuario,)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Usuário deletado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao deletar usuário: {err}")
    finally:
        cursor.close()
        conexao.close()