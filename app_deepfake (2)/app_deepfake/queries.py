from database_config import conectar_banco

def consulta_midia_por_tipo(tipo='deepfake'):
    """
    Consulta todas as mídias de um tipo específico, como 'deepfake'.
    """
    with conectar_banco() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Midia WHERE tipo = %s", (tipo,))
            return cur.fetchall()

def consulta_distribuicao_geografica():
    """
    Consulta a distribuição geográfica das mídias, juntando tabelas necessárias.
    """
    with conectar_banco() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT m.id, m.descricao, l.pais
                FROM Midia m
                JOIN midia_localizacao ml ON m.id = ml.midia_id
                JOIN localizacao l ON ml.localizacao_id = l.id
            """)
            return cur.fetchall()

def consulta_midia_com_imagens():
    """
    Consulta mídias que contêm imagens (armazenadas como blobs).
    """
    with conectar_banco() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, descricao, tipo FROM Midia WHERE tipo IS NOT NULL AND Midia.tipo = 'imagem'")
            return cur.fetchall()

def consulta_plataformas_por_midia():
    """
    Consulta para listar mídias por plataforma de origem.
    """
    with conectar_banco() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT m.id, m.descricao, l.plataforma AS plataforma
                FROM Midia m
                JOIN Midia_Localizacao ml ON m.id = ml.midia_id
                JOIN Localizacao l ON ml.localizacao_id = l.id
            """)
            return cur.fetchall()


def consulta_motivos_por_midia():
    """
    Consulta para listar os motivos da criação e disseminação de cada mídia.
    """
    with conectar_banco() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT m.id, m.descricao, mo.descricao AS motivo
                FROM Midia m
                JOIN Midia_Motivo mm ON m.id = mm.midia_id
                JOIN Motivo mo ON mm.motivo_id = mo.id
            """)
            return cur.fetchall()


def consulta_agentes_alvos():
    """
    Consulta para visualizar as interações entre agentes e alvos de mídia.
    """
    with conectar_banco() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT a.nome AS agente, al.nome AS alvo
                FROM agente a
                JOIN agente_alvo aa ON a.id = aa.agente_id
                JOIN alvo al ON aa.alvo_id = al.id
            """)
            return cur.fetchall()

def consulta_midia_por_pais_e_tipo():
    """
    Consulta para contagem de mídias por país e tipo.
    """
    with conectar_banco() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT l.pais, m.tipo, COUNT(m.id) AS total
                FROM Midia m
                JOIN midia_localizacao ml ON m.id = ml.midia_id
                JOIN localizacao l ON ml.localizacao_id = l.id
                GROUP BY l.pais, m.tipo
            """)
            return cur.fetchall()
