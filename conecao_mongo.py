# Copiar no Bash antes de rodar - pip install pymongo pandas mysql-connector-python
import mysql.connector
from pymongo import MongoClient
import pandas as pd
import math

MYSQL_HOST = "localhost" 
MYSQL_USER = "root" 
MYSQL_PASSWORD = "mariabd"  # <-- Mude a senha
MYSQL_DATABASE = "Dados_RFB" 

MONGO_URI = "mongodb://localhost:27017/" # Endereço padrão
MONGO_DATABASE = "mariabd_mongo"
CHUNK_SIZE = 10000  # Tamanho do lote por iteração

# Dicionário: {Nome da Tabela MySQL: Nome da Coleção MongoDB}
TABELAS_PARA_MIGRAR = {
    'empresa': 'empresas',
    'estabelecimento': 'estabelecimentos',
    'socios': 'socios',
    'simples': 'simples',
    'motivos': 'motivos_situacao',
    'munic': 'municipios',
    'pais': 'paises'
}

def conectar_mysql():
    """Conecta ao MySQL e retorna a conexão."""
    try:
        return mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
    except mysql.connector.Error as err:
        print(f"❌ Erro de Conexão MySQL: {err}")
        return None

def conectar_mongo():
    """Conecta ao MongoDB e retorna o objeto do Banco de Dados."""
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DATABASE]
        print(f"✅ Conectado ao MongoDB. Banco de Dados: {MONGO_DATABASE}")
        return db, client
    except Exception as err:
        print(f"❌ Erro de Conexão MongoDB: {err}")
        return None, None

def migrar_tabela(mysql_conn, mongo_db, mysql_tabela, mongo_colecao):
    """Lê a tabela do MySQL em lotes e insere no MongoDB."""
    
    print(f"\n[🔄 INICIANDO: {mysql_tabela} -> {mongo_colecao}]")
    

    query_count = f"SELECT COUNT(*) FROM {mysql_tabela}"
    total_registros = pd.read_sql(query_count, mysql_conn).iloc[0, 0]
    total_chunks = math.ceil(total_registros / CHUNK_SIZE)
    print(f"Total de registros: {total_registros:,} | Total de Lotes: {total_chunks}")
    
    collection = mongo_db[mongo_colecao]
    

    
    try:
        for i in range(total_chunks):
            offset = i * CHUNK_SIZE
            query_data = f"SELECT * FROM {mysql_tabela} LIMIT {CHUNK_SIZE} OFFSET {offset}"
            df = pd.read_sql(query_data, mysql_conn)
            records = df.to_dict('records')
            if records:
                collection.insert_many(records)
            
            print(f"   -> Lote {i + 1}/{total_chunks} concluído. {len(records)} documentos inseridos.")
        
        print(f"✅ SUCESSO: Migração da tabela '{mysql_tabela}' concluída. Documentos finais: {collection.count_documents({})}")
        
    except Exception as e:
        print(f"❌ FALHA na migração da tabela {mysql_tabela}: {e}")

if __name__ == "__main__":
    mysql_conn = conectar_mysql()
    mongo_db, mongo_client = conectar_mongo()

    if mysql_conn and mongo_db:
        for mysql_table, mongo_collection in TABELAS_PARA_MIGRAR.items():
            migrar_tabela(mysql_conn, mongo_db, mysql_table, mongo_collection)
        mysql_conn.close()
        mongo_client.close()
        print("\nProcesso de migração total concluído.")
    else:
        print("\nNão foi possível iniciar a migração devido a falha nas conexões.")

