USE teo_web;
INSERT INTO jogos_jogos (nome) VALUES ('Cores');
INSERT INTO jogos_jogos (nome) VALUES ("Memoria");
INSERT INTO jogos_jogos (nome) VALUES ("Numeros");
INSERT INTO jogos_jogos (nome) VALUES ("Onde Está?");
INSERT INTO jogos_jogos (nome) VALUES ("Quanto É?");
INSERT INTO jogos_jogos (nome) VALUES ("Quebra-Cabeça");
INSERT INTO jogos_jogos (nome) VALUES ("Vestir");

INSERT INTO paciente_pacientejoga (cpf_id, nomeJogo_id, tempoJogo, quantidadeAcertos, quantidadeErros, horario) VALUES ("12345678901", "Cores", 60, 6, 0, NOW());
INSERT INTO paciente_pacientejoga (cpf_id, nomeJogo_id, tempoJogo, quantidadeAcertos, quantidadeErros, horario) VALUES ("12345678902", "Memoria", 60, 12, 24, NOW());
INSERT INTO paciente_pacientejoga (cpf_id, nomeJogo_id, tempoJogo, quantidadeAcertos, quantidadeErros, horario) VALUES ("12345678903", "Numeros", 60, 1, 7, NOW());
INSERT INTO paciente_pacientejoga (cpf_id, nomeJogo_id, tempoJogo, quantidadeAcertos, quantidadeErros, horario) VALUES ("12345678901", "Vestir", 60, 4, 6, NOW());
