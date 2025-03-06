print("Iniciando o processamento de dados...")  # Verificação de início

import pandas as pd
from sqlalchemy import create_engine

# Caminho do arquivo CSV
df = pd.read_csv('data/IOT-temp.csv')  
print("Arquivo CSV carregado com sucesso!")  # Verificação de leitura do CSV

# Conexão com o banco de dados PostgreSQL
engine = create_engine('postgresql://postgres:Senha@localhost:5432/postgres')

# Inserir os dados do CSV na tabela do banco de dados PostgreSQL
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso!")  # Verificação de inserção no banco