import streamlit as st
import pandas as pd
import yfinance as yf

from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from plotly import graph_objs as go

DATA_INICIO = '2017-01-01'
DATA_FIM = date.today().strftime('%Y-%m-%d')

st.title('Previsão de preços de ações!')

# Criando um sidebar
st.sidebar.header('Parâmetros de entrada')

n_dias = st.sidebar.slider('Dias de previsão:', 30, 365)

def carrega_dados_acoes():
    # Carregando os dados
    path = 'acoes.csv'
    return pd.read_csv(path, delimiter=';')

df = carrega_dados_acoes()

acao = df['snome']
nome_acao_escolhida = st.sidebar.selectbox('Selecione a ação:', acao)

df_acao = df[df['snome'] == nome_acao_escolhida]
acao_escolhida = df_acao.iloc[0]['sigla-acao']

st.write(df_acao.iloc[0]['sigla-acao'])