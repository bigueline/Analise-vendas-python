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

# Verifica quantas vendas já existem na tabela.
cursor.execute("SELECT COUNT(*) FROM vendas1")
quantidade = cursor.fetchone()[0]

if quantidade == 0:
    # Cada tupla representa uma venda:
    # data, produto, categoria e valor.
    vendas = [
        ("2023-01-01", "Produto A", "Eletrônicos", 1500.00),
        ("2023-01-05", "Produto B", "Roupas", 350.00),
        ("2023-02-10", "Produto C", "Eletrônicos", 1200.00),
        ("2023-03-15", "Produto D", "Livros", 200.00),
        ("2023-03-20", "Produto E", "Eletrônicos", 800.00),
        ("2023-04-02", "Produto F", "Roupas", 400.00),
        ("2023-05-05", "Produto G", "Livros", 150.00),
        ("2023-06-10", "Produto H", "Eletrônicos", 1000.00),
        ("2023-07-20", "Produto I", "Roupas", 600.00),
        ("2023-08-25", "Produto J", "Eletrônicos", 700.00),
        ("2023-09-30", "Produto K", "Livros", 300.00),
        ("2023-10-05", "Produto L", "Roupas", 450.00),
        ("2023-11-15", "Produto M", "Eletrônicos", 900.00),
        ("2023-12-20", "Produto N", "Livros", 250.00),
    ]

    cursor.executemany("""
        INSERT INTO vendas1 (
            data_venda, produto, categoria, valor_venda
        ) VALUES (?, ?, ?, ?)
    """, vendas)

    conexao.commit()
    print("Vendas de exemplo inseridas!")
else:
    print("A tabela já contém vendas. Carga inicial ignorada.")

# Confere a quantidade depois da carga.
cursor.execute("SELECT COUNT(*) FROM vendas1")
total = cursor.fetchone()[0]

print(f"Total de vendas cadastradas: {total}")

# Fecha a conexão ao terminar.
conexao.close()

