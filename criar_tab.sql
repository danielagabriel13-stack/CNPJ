SET GLOBAL local_infile = 1;
SHOW VARIABLES LIKE 'local_infile';
CREATE DATABASE IF NOT EXISTS mariabd;
USE mariabd;
--
CREATE TABLE empresa (
    cnpj_basico CHAR(8),
    razao_social VARCHAR(255),
    natureza_juridica CHAR(4),
    qualificacao_responsavel CHAR(2),
    capital_social VARCHAR(20),
    porte_empresa CHAR(2),
    ente_federativo_responsavel VARCHAR(100)
) CHARACTER SET latin1;
--
CREATE TABLE estabelecimento (
    cnpj_basico CHAR(8),
    cnpj_ordem CHAR(4),
    cnpj_dv CHAR(2),
    identificador_matriz_filial CHAR(1),
    nome_fantasia VARCHAR(255),
    situacao_cadastral CHAR(2),
    data_situacao_cadastral CHAR(8),
    motivo_situacao_cadastral CHAR(2),
    nome_cidade_exterior VARCHAR(255),
    pais CHAR(3),
    data_inicio_atividade CHAR(8),
    cnae_fiscal_principal CHAR(7),
    cnae_fiscal_secundaria VARCHAR(1000),
    tipo_logradouro VARCHAR(50),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cep CHAR(8),
    uf CHAR(2),
    municipio CHAR(7),
    ddd_1 CHAR(4),
    telefone_1 CHAR(10),
    ddd_2 CHAR(4),
    telefone_2 CHAR(10),
    ddd_fax CHAR(4),
    fax CHAR(10),
    correio_eletronico VARCHAR(255),
    situacao_especial VARCHAR(255),
    data_situacao_especial CHAR(8)
) CHARACTER SET latin1;
--
CREATE TABLE socios (
    cnpj_basico CHAR(8),
    identificador_socio CHAR(1),
    nome_socio_razao_social VARCHAR(255),
    cpf_cnpj_socio VARCHAR(20),
    qualificacao_socio CHAR(2),
    data_entrada_sociedade CHAR(8),
    pais CHAR(3),
    representante_legal VARCHAR(20),
    nome_do_representante VARCHAR(255),
    qualificacao_representante_legal CHAR(2),
    faixa_etaria CHAR(2)
) CHARACTER SET latin1;
--
CREATE TABLE simples (
    cnpj_basico CHAR(8),
    opcao_pelo_simples CHAR(1),
    data_opcao_simples CHAR(8),
    data_exclusao_simples CHAR(8),
    opcao_mei CHAR(1),
    data_opcao_mei CHAR(8),
    data_exclusao_mei CHAR(8)
) CHARACTER SET latin1;
--
CREATE TABLE natju (
    codigo CHAR(4),
    descricao VARCHAR(255)
) CHARACTER SET latin1;
--
CREATE TABLE cnae (
    codigo CHAR(7),
    descricao VARCHAR(255)
) CHARACTER SET latin1;
--
CREATE TABLE pais (
    codigo CHAR(3),
    descricao VARCHAR(255)
) CHARACTER SET latin1;
--
CREATE TABLE munic (
    codigo CHAR(7),
    descricao VARCHAR(255)
) CHARACTER SET latin1;
--
CREATE TABLE quals (
    codigo CHAR(2),
    descricao VARCHAR(255)
) CHARACTER SET latin1;

