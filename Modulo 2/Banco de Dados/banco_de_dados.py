import sqlite3

try:
    con = sqlite3.connect("meu_banco.db")
    cur = con.cursor()
    #cur.execute("CREATE TABLE pessoa (id, nome, idade, cpf)")
    con.commit()
except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')

try:
    con = sqlite3.connect("meu_banco.db")
    cur =con.cursor() 
    # cur.execute("INSERT INTO pessoa VALUES (1, 'Guilherme', 15, '550-219-148.36')")
    con.commit()
except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')

try:
    con = sqlite3.connect("meu_banco.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM pessoa")
    pessoas = res.fetchone()
    print(pessoas)
    cur.close()
except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')

try:
    con = sqlite3.connect("meu_banco.db")
    cur = con.cursor() 
    cur.execute("DELETE FROM pessoa WHERE id 1")
    con.commit()
    cur.close()
except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')