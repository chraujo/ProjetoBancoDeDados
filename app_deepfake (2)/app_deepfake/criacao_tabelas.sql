CREATE TABLE Alvo (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150),
    tipo VARCHAR(50) -- indivíduo, grupo, etc.
);

CREATE TABLE Motivo (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(100) NOT NULL,
    descricao TEXT
);

CREATE TABLE Regulamento (
    id SERIAL PRIMARY KEY,
    nome_pais VARCHAR(100) NOT NULL,
    leis TEXT,
    detalhes TEXT
);

CREATE TABLE Tag (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE Agente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    funcao VARCHAR(100) -- criador, disseminador, etc.
);

CREATE TABLE Agente_Alvo (
    agente_id INT REFERENCES Agente(id) ON DELETE CASCADE,
    alvo_id INT REFERENCES Alvo(id) ON DELETE CASCADE,
    PRIMARY KEY (agente_id, alvo_id)
);

CREATE TABLE Localizacao (
    id SERIAL PRIMARY KEY,
    plataforma VARCHAR(100), -- redes sociais, websites, etc.
    url VARCHAR(255),
    pais VARCHAR(100)
);

CREATE TABLE Midia (
    id SERIAL PRIMARY KEY, 
    tipo VARCHAR(50), -- vídeo, imagem, áudio, etc.
    caminho_arquivo VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_criacao DATE NOT NULL,
    data_encontrada DATE,
    eh_deepfake BOOLEAN NOT NULL,
    agente_id INT REFERENCES Agente(id) -- Relacionamento n:1 com Agente
);

CREATE TABLE Midia_Localizacao (
    midia_id INT REFERENCES Midia(id) ON DELETE CASCADE,
    localizacao_id INT REFERENCES Localizacao(id) ON DELETE CASCADE,
    PRIMARY KEY (midia_id, localizacao_id)
);

CREATE TABLE Midia_Motivo (
    midia_id INT REFERENCES Midia(id) ON DELETE CASCADE,
    motivo_id INT REFERENCES Motivo(id) ON DELETE CASCADE,
    PRIMARY KEY (midia_id, motivo_id)
);

CREATE TABLE Midia_Regulamento (
    midia_id INT REFERENCES Midia(id) ON DELETE CASCADE,
    regulamento_id INT REFERENCES Regulamento(id) ON DELETE CASCADE,
    PRIMARY KEY (midia_id, regulamento_id)
);

CREATE TABLE Midia_Tag (
    midia_id INT REFERENCES Midia(id) ON DELETE CASCADE,
    tag_id INT REFERENCES Tag(id) ON DELETE CASCADE,
    PRIMARY KEY (midia_id, tag_id)
);

