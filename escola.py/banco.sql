CREATE DATABASE IF NOT EXISTS sistema_escolar;
USE sistema_escolar;
CREATE TABLE IF NOT EXISTS alunos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    turma VARCHAR(50) NOT NULL,
    media FLOAT,
    situacao VARCHAR(20)
);
SELECT * FROM alunos;