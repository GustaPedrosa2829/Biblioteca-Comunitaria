from database_connection import conectar
from datetime import datetime, timedelta

def obras_mais_emprestadas(limit=10):
    """Retorna as obras mais emprestadas com quantidade de empréstimos"""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
        SELECT 
            o.titulo,
            COUNT(e.id_emprestimo) as total_emprestimos,
            o.ano_publicacao,
            ed.nome_editora
        FROM Obras o
        JOIN Exemplares ex ON o.id_obra = ex.id_obra
        JOIN Emprestimos e ON ex.id_exemplar = e.id_exemplar
        JOIN Editoras ed ON o.id_editora = ed.id_editora
        GROUP BY o.id_obra, o.titulo, o.ano_publicacao, ed.nome_editora
        ORDER BY total_emprestimos DESC
        LIMIT %s
        """
        cursor.execute(sql, (limit,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def usuarios_em_atraso():
    """Identifica usuários com empréstimos em atraso"""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
        SELECT 
            u.nome,
            u.telefone,
            o.titulo,
            e.data_devolucao_prevista,
            DATEDIFF(CURRENT_DATE, e.data_devolucao_prevista) as dias_atraso
        FROM Usuarios u
        JOIN Emprestimos e ON u.id_usuario = e.id_usuario
        JOIN Exemplares ex ON e.id_exemplar = ex.id_exemplar
        JOIN Obras o ON ex.id_obra = o.id_obra
        WHERE e.data_devolucao_prevista < CURRENT_DATE
        AND e.data_devolucao_real IS NULL
        ORDER BY dias_atraso DESC
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def disponibilidade_obra(titulo):
    """Verifica disponibilidade de uma obra específica"""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
        SELECT 
            o.titulo,
            COUNT(ex.id_exemplar) as total_exemplares,
            SUM(CASE WHEN ex.status = 'disponível' THEN 1 ELSE 0 END) as exemplares_disponiveis,
            COUNT(r.id_reserva) as reservas_ativas
        FROM Obras o
        LEFT JOIN Exemplares ex ON o.id_obra = ex.id_obra
        LEFT JOIN Reservas r ON ex.id_exemplar = r.id_exemplar
        WHERE o.titulo LIKE %s
        GROUP BY o.id_obra, o.titulo
        """
        cursor.execute(sql, (f"%{titulo}%",))
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def historico_usuario(id_usuario):
    """Retorna histórico completo de empréstimos de um usuário"""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
        SELECT 
            o.titulo,
            e.data_emprestimo,
            e.data_devolucao_prevista,
            e.data_devolucao_real,
            CASE 
                WHEN e.data_devolucao_real IS NULL AND CURRENT_DATE > e.data_devolucao_prevista 
                THEN 'Em atraso'
                WHEN e.data_devolucao_real IS NULL 
                THEN 'Em andamento'
                WHEN e.data_devolucao_real > e.data_devolucao_prevista 
                THEN 'Devolvido com atraso'
                ELSE 'Devolvido no prazo'
            END as status
        FROM Emprestimos e
        JOIN Exemplares ex ON e.id_exemplar = ex.id_exemplar
        JOIN Obras o ON ex.id_obra = o.id_obra
        WHERE e.id_usuario = %s
        ORDER BY e.data_emprestimo DESC
        """
        cursor.execute(sql, (id_usuario,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def relatorio_uso_biblioteca(dias=30):
    """Gera relatório de uso da biblioteca nos últimos X dias"""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
        SELECT 
            COUNT(DISTINCT e.id_emprestimo) as total_emprestimos,
            COUNT(DISTINCT e.id_usuario) as usuarios_ativos,
            AVG(CASE 
                WHEN e.data_devolucao_real IS NOT NULL 
                THEN DATEDIFF(e.data_devolucao_real, e.data_emprestimo)
                ELSE DATEDIFF(CURRENT_DATE, e.data_emprestimo)
            END) as media_dias_emprestimo,
            COUNT(DISTINCT r.id_reserva) as total_reservas,
            COUNT(DISTINCT 
                CASE WHEN e.data_devolucao_real > e.data_devolucao_prevista 
                THEN e.id_emprestimo END
            ) as devolucoes_atrasadas
        FROM Emprestimos e
        LEFT JOIN Reservas r ON r.data_reserva >= DATE_SUB(CURRENT_DATE, INTERVAL %s DAY)
        WHERE e.data_emprestimo >= DATE_SUB(CURRENT_DATE, INTERVAL %s DAY)
        """
        cursor.execute(sql, (dias, dias))
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def sugestoes_aquisicao():
    """Identifica obras com alta demanda para possível aquisição de novos exemplares"""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
        SELECT 
            o.titulo,
            COUNT(DISTINCT e.id_emprestimo) as total_emprestimos,
            COUNT(DISTINCT r.id_reserva) as total_reservas,
            COUNT(DISTINCT ex.id_exemplar) as exemplares_existentes,
            ROUND(
                (COUNT(DISTINCT e.id_emprestimo) + COUNT(DISTINCT r.id_reserva)) / 
                COUNT(DISTINCT ex.id_exemplar), 2
            ) as indice_demanda
        FROM Obras o
        JOIN Exemplares ex ON o.id_obra = ex.id_obra
        LEFT JOIN Emprestimos e ON ex.id_exemplar = e.id_exemplar
        LEFT JOIN Reservas r ON ex.id_exemplar = r.id_exemplar
        GROUP BY o.id_obra, o.titulo
        HAVING indice_demanda > 5
        ORDER BY indice_demanda DESC
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()