# **CNPJ — Trabalho de Banco de Dados Não Relacional**

## **ETL das Bases do CNPJ — Comparação MySQL x MongoDB**

Este projeto apresenta um fluxo de **ETL** desenvolvido para processar as bases públicas do **CNPJ** (Receita Federal) e comparar o desempenho entre um banco **relacional (MySQL)** e um banco **não relacional (MongoDB)** ao lidar com grandes volumes de dados.

---

## **Objetivo**

- Demonstrar, na prática, como diferentes modelos de banco de dados respondem ao processamento de informações corporativas reais, avaliando:
  - **Estrutura**
  - **Desempenho**
  - **Facilidade de carga**
  - **Flexibilidade na organização dos dados**

---

## **Descrição do Processo**

### **1) Etapa MySQL (Relacional)**

- Download e descompactação dos arquivos da Receita Federal  
- Modelagem das tabelas e definição de chaves  
- Preparação e inserção dos dados no modelo relacional  
- **Tempo de upload:** 7 horas  

### **2) Etapa MongoDB (Não Relacional)**

- Conversão dos arquivos para **JSON**  
- Inserção direta no MongoDB como documentos  
- **Tempo de upload:** 2 minutos e 30 segundos  

---

## **Principais Resultados**

O **MongoDB** demonstrou maior agilidade e flexibilidade na ingestão de dados, enquanto o **MySQL** exigiu maior estruturação, porém oferece maior integridade e padronização.

---

## **Conclusão**

O projeto evidenciou as diferenças práticas entre bancos relacionais e não relacionais:

- **MySQL:** mais rígido, estruturado e exige modelagem detalhada.  
- **MongoDB:** flexível, rápido e ideal para grandes volumes com estrutura variável.  

A escolha entre os dois depende do tipo de aplicação, necessidade de consistência e formato dos dados utilizados.


Inserção direta no MongoDB como documentos

Tempo de upload: 2 min 30 s
