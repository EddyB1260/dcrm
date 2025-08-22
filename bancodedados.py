import pymysql

try:
    # Conecta sem especificar o banco
    conexao_inicial = pymysql.connect(
        host="localhost",
        user="root",
        password="Queijominas@1"
    )
    cursor = conexao_inicial.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS dcrm")
    print("Banco de dados criado com sucesso!")
    cursor.close()
    conexao_inicial.close()

    # Agora conecta ao banco recém-criado
    BancodDados = pymysql.connect(
        host="localhost",
        user="root",
        password="Queijominas@1",
        database="dcrm"
    )
    print("Conexão ao banco 'dcrm' estabelecida com sucesso!")

except pymysql.Error as err:
    print(f"Erro ao criar ou conectar ao banco de dados: {err}")