import sqlite3

# Abre o banco ou cria o arquivo, caso ainda não exista.
conexao = sqlite3.connect("dados_vendas.db")

# O cursor permite executar comandos SQL.
cursor = conexao.cursor()

print("Conexão criada com sucesso!")

# Cria a tabela somente se ela ainda não existir.
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
""")

conexao.commit()

print("Tabela de vendas pronta!")