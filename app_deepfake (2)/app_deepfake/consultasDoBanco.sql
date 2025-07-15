-- Consultar as mídias pelas plataformas nas quais elas foram encontradas
SELECT m.id, m.tipo, l.plataforma, l.pais
FROM Midia m
JOIN Midia_Localizacao ml ON m.id = ml.midia_id
JOIN Localizacao l ON ml.localizacao_id = l.id
WHERE l.plataforma = ;-- INSIRA O NOME DA PLATAFORMA AQUI

-- Consultar as mídias pelos países nas quais elas foram encontradas
SELECT m.id, m.tipo, l.plataforma, l.pais
FROM Midia m
JOIN Midia_Localizacao ml ON m.id = ml.midia_id
JOIN Localizacao l ON ml.localizacao_id = l.id
WHERE l.pais IN ('Brasil', 'Argentina', 'Paraguai', 'Peru', 'Uruguai');-- INSIRA O NOME DO PAIS AQUI

-- Consultar as mídias que realmente são fakes
SELECT id, tipo, descricao, data_encontrada
FROM Midia
WHERE eh_deepfake = TRUE;

-- Consultar a quantide de mídias por tipo
SELECT m.tipo, COUNT(m.id) AS qtd_midias
FROM Midia m
JOIN Midia_Localizacao ml ON m.id = ml.midia_id
GROUP BY m.tipo;

-- Consultar a quantidade de mídias por país e pelo tipo
SELECT m.tipo, l.pais, COUNT(m.id) AS qtd_midias
FROM Midia m
JOIN Midia_Localizacao ml ON m.id = ml.midia_id
JOIN Localizacao l ON ml.localizacao_id = l.id
GROUP BY m.tipo, l.pais;

-- Relacionar o agente e os alvos desse agente
SELECT a.nome AS nome_agente, al.nome AS nome_alvo
FROM Agente a
JOIN Agente_Alvo aa ON a.id = aa.agente_id
JOIN Alvo al ON aa.alvo_id = al.id
WHERE a.nome = ; -- INSIRA AQUI O NOME DO AGENTE

-- Consultar as mídias pelo motivo
SELECT m.id, m.tipo, m.descricao, mo.descricao AS motivo
FROM Midia m
JOIN Midia_Motivo mm ON m.id = mm.midia_id
JOIN Motivo mo ON mm.motivo_id = mo.id
WHERE mo.descricao IN ('cultural', 'político', 'social', 'socioambiental'); -- INSIRA AQUI O MOTIVO

-- Consultar os países que tem leis mais fortes ou mais fracas
SELECT nome_pais, leis, detalhes
FROM Regulamento
WHERE leis = 'há regulação sobre deepfakes';

-- Filtrar as mídias pelas datas
SELECT id, tipo, descricao, data_criacao, data_encontrada
FROM Midia
WHERE data_criacao >= '01/01/2020' AND data_encontrada > data_criacao;
