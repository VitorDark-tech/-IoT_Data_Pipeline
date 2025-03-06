Pipeline de Dados IoT

Introdução
Este projeto apresenta um pipeline de dados que integra dispositivos IoT para leitura de temperaturas, utilizando Docker, DBeaver e Streamlit para criação de um dashboard interativo.

---

 Tecnologias Utilizadas
- Python (pandas, sqlalchemy, psycopg2, plotly, streamlit) 

-Docker para conteinerização 

-DBeaver para gerenciamento e manipulação do banco de dados 

-Kaggle para o conjunto de dados 

-Git para versionamento de código 

---

Passo a Passo da Instalação

1. Clonar o Repositório

git clone https://github.com/VitorDark-tech/-IoT_Data_Pipeline.git
cd -IoT_Data_Pipeline

2. Criar Ambiente Virtual

pip install virtualenv
virtualenv venv
venv\\Scripts\\activate  # Windows

3. Executar o Docker 

Substitua sua_senha pela senha que deseja usar para o banco. 

docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres 


4. Conexão com Banco de Dados DBeaver
Abra o DBeaver.
Vá para Database → New Database Connection.
Escolha PostgreSQL.
Preencha as informações:
Host: localhost
Port: 5432
Database: postgres
User: postgres
Password: sua_senha
Clique em Test Connection para verificar se está tudo certo.
Salve e conecte-se ao banco.

5. Carregar Dados para o Banco 

python process_data.py 

6. Rodar o Dashboard 

streamlit run dashboard.py 

Execução 

Certifique-se que o Docker e o container PostgreSQL estejam rodando. 

Execute o process_data.py para carregar os dados no banco. 

Acesse o banco pelo DBeaver para validar os dados. 

Inicie o dashboard.py com Streamlit para visualizar os gráficos. 

Visualizações(Capturas de Telas de Dashboard):
### Gráfico de Média de Temperatura por Dispositivo
![Gráfico 01: Temperatura Por dispostivo](./img/Grafico01.png)

### Gráfico de Leituras por Hora
![Gráfico 02: Leituras por Hora](./img/Grafico02.png)

### Gráfico de Temperaturas Máximas e Mínimas
![Gráfico 03: Temperaturas Máximas e Mínimas Por dia](./img/Grafico03.png)


Views SQL e Propósitos

1. Média de Temperatura por Dispositivo

CREATE VIEW avg_temp_por_dispositivo AS 
SELECT "room_id/id" AS device_id, AVG(temp) AS avg_temp 
FROM temperature_readings 
GROUP BY device_id;

Propósito: Essa view calcula a temperatura média registrada por cada dispositivo, permitindo análises comparativas entre diferentes sensores.

2. Leituras por Hora

CREATE VIEW leituras_por_hora AS 
SELECT EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora, 
       COUNT(*) AS total_leituras 
FROM temperature_readings 
GROUP BY hora 
ORDER BY hora;

Propósito: Essa view contabiliza quantas leituras foram feitas por hora do dia, ajudando a identificar padrões de atividade dos dispositivos. 

3. Temperaturas Máximas e Mínimas por Dia

CREATE VIEW temp_max_min_por_dia AS 
SELECT DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS data, 
       MAX(temp) AS temp_maxima, 
       MIN(temp) AS temp_minima 
FROM temperature_readings 
GROUP BY data 
ORDER BY data;

Propósito: Essa view exibe a temperatura máxima e mínima registrada a cada dia, útil para identificar variações climáticas diárias.

Insights Obtidos 

Padrões de Temperatura: Identificação dos dispositivos que registram temperaturas mais altas ou mais baixas. 

Horários de Pico: Determinação das horas com maior volume de leituras. 

Variações Diárias: Análise das temperaturas máximas e mínimas para identificar mudanças climáticas ao longo dos dias. 