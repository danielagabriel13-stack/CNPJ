import mysql.connector

DB_HOST = "localhost" 
DB_PORT = 3306
DB_USER = "root" 
DB_PASSWORD = "Faculdade@2024"  # <-- SUBSTITUA PELA SUA SENHA REAL!
DB_NAME = "mariabd" 

def conectar_bd():
    """Tenta estabelecer a conexão com o banco de dados."""
    try:
        mydb = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"❌ Erro ao conectar ao MySQL (Verifique credenciais/status do servidor): {err}")
        return None

def analisar_cardinalidade_1_N(mydb, tabela_lado_1, tabela_lado_N, chave_comum):
    """
    Analisa a cardinalidade de Um para Muitos (1:N) entre duas tabelas
    comparando a contagem de chaves únicas e total de registros.
    """
    cursor = mydb.cursor()
    print(f"\n--- Análise Cardinalidade {tabela_lado_1}:{tabela_lado_N} ({chave_comum}) ---")

    # 1. Contagem de registros no lado "1" (chaves primárias únicas)
    sql_pk = f"SELECT COUNT(DISTINCT {chave_comum}) FROM {tabela_lado_1};"
    cursor.execute(sql_pk)
    total_pk = cursor.fetchone()[0]
    print(f"Total de chaves únicas no lado '1' ({tabela_lado_1}): {total_pk:,}")

    # 2. Contagem de registros e chaves únicas no lado "N" (chaves estrangeiras)
    sql_fk_stats = f"SELECT COUNT({chave_comum}), COUNT(DISTINCT {chave_comum}) FROM {tabela_lado_N};"
    cursor.execute(sql_fk_stats)
    total_fk_all, total_fk_unique = cursor.fetchone()
    
    print(f"Total de registros no lado 'N' ({tabela_lado_N}): {total_fk_all:,}")
    print(f"Total de chaves únicas no lado 'N' ({tabela_lado_N}): {total_fk_unique:,}")

    # 3. Inferir Cardinalidade
    if total_fk_all > total_fk_unique:
        media_relacao = total_fk_all / total_fk_unique
        print(f"Resultado: Relação 1:N (Um para Muitos) - Média de {media_relacao:.2f} registros em {tabela_lado_N} por chave em {tabela_lado_1}")
    elif total_fk_all > 0 and total_fk_all == total_fk_unique:
        print("Resultado: Relação 1:1 (Um para Um) - Cada registro no lado 'N' se relaciona com apenas um no lado '1'.")
    else:
        print("Resultado: Dados insuficientes ou erro na análise.")

def analisar_cardinalidade_N_1_dominio(mydb, tabela_lado_N, tabela_lado_1, chave_fk):
    """
    Analisa a cardinalidade de Muitos para Um (N:1) para tabelas de domínio (código:descrição).
    """
    cursor = mydb.cursor()
    print(f"\n--- Análise Cardinalidade {tabela_lado_N}:{tabela_lado_1} ({chave_fk}) ---")

    # 1. Contagem total de registros no lado "Muitos"
    sql_total_registros = f"SELECT COUNT(*) FROM {tabela_lado_N};"
    cursor.execute(sql_total_registros)
    total_n = cursor.fetchone()[0]
    print(f"Total de registros em {tabela_lado_N}: {total_n:,}")

    # 2. Contagem de códigos de domínio existentes
    sql_total_pk = f"SELECT COUNT(*) FROM {tabela_lado_1};"
    cursor.execute(sql_total_pk)
    total_1 = cursor.fetchone()[0]
    print(f"Total de códigos em {tabela_lado_1} (Domínio): {total_1:,}")

    # 3. Contagem de códigos utilizados/referenciados
    sql_fk_unique = f"SELECT COUNT(DISTINCT {chave_fk}) FROM {tabela_lado_N};"
    cursor.execute(sql_fk_unique)
    utilizados = cursor.fetchone()[0]
    print(f"Códigos de {tabela_lado_1} utilizados em {tabela_lado_N}: {utilizados:,}")

    # 4. Inferir Cardinalidade
    if total_n > 0 and utilizados <= total_1:
        print(f"Resultado: Relação N:1 (Muitos para Um) - {tabela_lado_N} referencia {tabela_lado_1}.")
    else:
        print("Resultado: Inconsistente ou erro na análise.")


if __name__ == "__main__":
    mydb = conectar_bd()
    
    if mydb:
        # 1. EMPRESA (1) -> ESTABELECIMENTO (N)
        analisar_cardinalidade_1_N(mydb, 
                                  tabela_lado_1='empresa', 
                                  tabela_lado_N='estabelecimento', 
                                  chave_comum='cnpj_basico')

        # 2. EMPRESA (1) -> SOCIOS (N)
        analisar_cardinalidade_1_N(mydb, 
                                  tabela_lado_1='empresa', 
                                  tabela_lado_N='socios', 
                                  chave_comum='cnpj_basico')
        
        # 3. ESTABELECIMENTO (N) -> MUNIC (1)
        analisar_cardinalidade_N_1_dominio(mydb, 
                                          tabela_lado_N='estabelecimento', 
                                          tabela_lado_1='munic', 
                                          chave_fk='municipio')
        
        mydb.close()
        print("\nProcesso de análise concluído e desconexão realizada.")
    else:
        print("\nNão foi possível prosseguir com a análise devido a falha na conexão.")