import sqlite3

try:
    con = sqlite3.connect("meu_banco.db")
    cur = con.cursor()
    # cur.execute("CREATE TABLE pessoa (id, nome, idade, cpf)")
    # cur.execute("INSERT INTO pessoa VALUES (1, 'Guilherme', 15, '550-219-148.36')")
    # cur.execute("INSERT INTO pessoa VALUES (2, 'Ana Clara', 16, '320-541-998.21')")
    # cur.execute("INSERT INTO pessoa VALUES (3, 'João Pedro', 17, '189-452-317.54')")
    # cur.execute("INSERT INTO pessoa VALUES (4, 'Maria Eduarda', 14, '756-888-147.90')")
    # cur.execute("INSERT INTO pessoa VALUES (5, 'Lucas Silva', 18, '624-215-369.40')")
    # cur.execute("INSERT INTO pessoa VALUES (6, 'Beatriz Souza', 15, '925-333-184.70')")
    # cur.execute("INSERT INTO pessoa VALUES (7, 'Pedro Henrique', 16, '417-582-991.35')")
    # cur.execute("INSERT INTO pessoa VALUES (8, 'Larissa Alves', 17, '835-419-620.82')")
    # cur.execute("INSERT INTO pessoa VALUES (9, 'Rafael Lima', 19, '610-284-775.12')")
    # cur.execute("INSERT INTO pessoa VALUES (10, 'Vitória Santos', 18, '743-120-956.47')")
    # cur.execute("INSERT INTO pessoa VALUES (11, 'Caio Fernandes', 14, '832-495-602.73')")
    
    cur.execute("DELETE FROM pessoa WHERE Nome = 'Maria Eduarda'")
    res = cur.execute("SELECT * FROM pessoa")
    pessoas = res.fetchall()
    
    for p in pessoas:
        print(p)

    cur.close()
    con.commit()
except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')

