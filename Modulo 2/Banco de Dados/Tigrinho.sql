-- Banco de Dados: TIGRINHO_ESTELHEONATARIO

CREATE TABLE Usuario (
    id_usuario          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                TEXT NOT NULL,
    email               TEXT NOT NULL UNIQUE,
    senha               TEXT NOT NULL,
    saldo               REAL DEFAULT 0,
    data_cadastro       TEXT DEFAULT CURRENT_TIMESTAMP,
    status              TEXT DEFAULT 'ativo'
);

CREATE TABLE Jogos (
    id_jogo             INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                TEXT NOT NULL,
    aposta_min          REAL NOT NULL,
    aposta_max          REAL NOT NULL,
    retorno_max         REAL,
    ativo               BOOLEAN DEFAULT 1
);

CREATE TABLE Partidas (
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

CREATE TABLE Transacoes (
    id_transacao        INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario          INTEGER,
    tipo                TEXT, 
    valor               REAL NOT NULL,
    forma_pagamento     TEXT,
    data                TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Rankings (
    id_usuario          INTEGER,
    pontuacao           INTEGER DEFAULT 0,
    nivel               TEXT DEFAULT 'Bronze',
    ultima_atualizacao  TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Estatisticas (
    id_usuario          INTEGER,
    porcentagem_ganho   REAL DEFAULT 0,
    porcentagem_perca   REAL DEFAULT 0,
    total_real          REAL DEFAULT 0,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);
