import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Atualize o nome de usuário, senha e o nome do banco de dados
engine = create_engine('postgresql://postgres:Senha@localhost:5432/postgres')

def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

st.title('Dashboard de Temperaturas IoT')

# Visualização da média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp', title="Média de Temperatura por Dispositivo")
st.plotly_chart(fig1)

# Visualização das leituras por hora
st.header('Leituras por Hora')
df_leituras_hora = load_data('leituras_por_hora')
fig2 = px.line(df_leituras_hora, x='hora', y='total_leituras', title="Leituras por Hora")
st.plotly_chart(fig2)

# Visualização da temperatura máxima e mínima por dia
st.header('Temperatura Máxima e Mínima por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_maxima', 'temp_minima'], title="Temperatura Máxima e Mínima por Dia")
st.plotly_chart(fig3)