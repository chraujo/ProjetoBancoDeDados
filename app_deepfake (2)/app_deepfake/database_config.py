import psycopg2

def conectar_banco():
    return psycopg2.connect(
        dbname="deepfakes",
        user="postgres",
        password="senha",
        host="localhost"
    )
