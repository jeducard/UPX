create database usuarios;
use usuarios;
CREATE TABLE IF NOT EXISTS info_Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    celular VARCHAR(20) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    foto_documento LONGBLOB,
    foto_reconhecimento LONGBLOB,
    biometria TEXT,
    modo VARCHAR(10) DEFAULT 'light'
);
describe info_Users;
select * from info_Users;
insert into info_Users(id, nome, email, celular, senha, foto_documento, foto_reconhecimento, biometria, modo)
values ('01', 'teste1', 'email', 'celular', 'senha', 'documento', 'reconhecimento', 'biometria','modo');