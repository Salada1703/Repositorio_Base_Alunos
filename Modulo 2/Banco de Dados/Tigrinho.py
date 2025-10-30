import sqlite3

try:
    con = sqlite3.connect('Tigrinho.db')
    cur = con.cursor()

    con.executescript("""
    CREATE TABLE IF NOT EXISTS Usuario (
        id_usuario          INTEGER PRIMARY KEY AUTOINCREMENT,
        nome                TEXT NOT NULL,
        email               TEXT NOT NULL UNIQUE,
        senha               TEXT NOT NULL,
        saldo               REAL DEFAULT 0,
        data_cadastro       TEXT DEFAULT CURRENT_TIMESTAMP,
        status              TEXT DEFAULT 'ativo'
    );

    CREATE TABLE IF NOT EXISTS Jogos (
        id_jogo             INTEGER PRIMARY KEY AUTOINCREMENT,
        nome                TEXT NOT NULL,
        aposta_min          REAL NOT NULL,
        aposta_max          REAL NOT NULL,
        retorno_max         REAL,
        ativo               BOOLEAN DEFAULT 1
    );

    CREATE TABLE IF NOT EXISTS Partidas (
        id_partida          INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario          INTEGER,
        id_jogo             INTEGER,
        aposta              REAL NOT NULL,
        resultado           TEXT,
        ganho               REAL,
        perda               REAL,
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
        FOREIGN KEY (id_jogo) REFERENCES Jogos(id_jogo)
    );

    CREATE TABLE IF NOT EXISTS Transacoes (
        id_transacao        INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario          INTEGER,
        tipo                TEXT, 
        valor               REAL NOT NULL,
        forma_pagamento     TEXT,
        data                TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
    );

    CREATE TABLE IF NOT EXISTS Rankings (
        id_usuario          INTEGER,
        pontuacao           INTEGER DEFAULT 0,
        nivel               TEXT DEFAULT 'Bronze',
        ultima_atualizacao  TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
    );

    CREATE TABLE IF NOT EXISTS Estatisticas (
        id_usuario          INTEGER,
        porcentagem_ganho   REAL DEFAULT 0,
        porcentagem_perca   REAL DEFAULT 0,
        total_real          REAL DEFAULT 0,
        FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
    );

    INSERT INTO Usuario (nome, email, senha, saldo)
    VALUES
    ('Guilherme Sampaio', 'gui@email.com', '1234', 150.00),
    ('Gabi Souza', 'gabi@email.com', 'abcd', 220.00),
    ('Pedro Henrique', 'pedro@email.com', 'senha', 90.00);

    INSERT INTO Jogos (nome, aposta_min, aposta_max, retorno_max)
    VALUES
    ('Caça Tigre', 1.00, 100.00, 1000.00),
    ('Roleta Selvagem', 5.00, 200.00, 1500.00),
    ('Tigre da Sorte', 2.00, 150.00, 1200.00);

    INSERT INTO Partidas (id_usuario, id_jogo, aposta, resultado, ganho, perda)
    VALUES
    (1, 1, 20.00, 'Vitória', 40.00, 0.00),
    (2, 2, 50.00, 'Derrota', 0.00, 50.00),
    (3, 3, 15.00, 'Vitória', 30.00, 0.00);

    INSERT INTO Transacoes (id_usuario, tipo, valor, forma_pagamento)
    VALUES
    (1, 'Depósito', 100.00, 'Pix'),
    (2, 'Aposta', 50.00, 'Saldo'),
    (3, 'Depósito', 200.00, 'Cartão');

    INSERT INTO Rankings (id_usuario, pontuacao, nivel)
    VALUES
    (1, 1200, 'Prata'),
    (2, 800, 'Bronze'),
    (3, 1600, 'Ouro');

    INSERT INTO Estatisticas (id_usuario, porcentagem_ganho, porcentagem_perca, total_real)
    VALUES
    (1, 70.0, 30.0, 500.0),
    (2, 45.0, 55.0, 300.0),
    (3, 80.0, 20.0, 900.0);
    """)

    con.commit()
    cur.close()

except sqlite3.Error as e:
    print("Erro ao criar ou popular o banco de dados:", e)
