/*COMANDO PARA CRIAR A BASE DE DADOS*/
create DATABASE ESCOLA


/*COMANDO PARA CRIAR A TABELA ALUNO*/
create table ALUNO (
    id INT not null auto_increment,
    nome varchar(30) not null,
    email varchar(50) not null,
    endereco varchar(100) not null,
    PRIMARY KEY (id)
)