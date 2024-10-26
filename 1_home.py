import streamlit as st
import pandas as pd

# Configuração inicial da página
st.set_page_config(
    page_title="Início - Projeto de Análise de Terrorismo",
    page_icon="📊",
    layout="wide"
)

# Links para os arquivos .parquet no formato bruto
file_urls = {
    'df_totals_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_totals_pt.parquet'
}

# Função para carregar dados de uma URL
def load_data(url):
    return pd.read_parquet(url)

# Carregar dados necessários para a página inicial
df_totals = load_data(file_urls['df_totals_pt'])

# Configuração da barra lateral (compartilhada entre as páginas)
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #ECEFF1;
        color: #37474F;
        font-size: 0.6em; /* Reduzido para metade do tamanho original */
    }
    .sidebar h1, .sidebar h2, .sidebar h3, .sidebar h4, .sidebar h5, .sidebar h6 {
        color: #1E88E5;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo da Unifor centralizada acima dos elementos
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <img src="https://www.unifor.br/o/unifor-theme/images/unifor-logo-horizontal.svg" width="80px">
    </div>
    """,
    unsafe_allow_html=True
)

# Introdução do Projeto
st.title("Análise de Terrorismo Global")
st.markdown("""
Bem-vindo ao projeto de análise de dados de terrorismo global. Esta aplicação oferece uma visão detalhada de eventos
terroristas ao redor do mundo, explorando dados como tipo de ataque, região, número de mortes e mais.
""")

# Tabela Resumo (carregada do arquivo 'df_totals_pt')
st.subheader("Resumo dos Conjuntos de Dados")
st.dataframe(df_totals)

# Continuação do conteúdo específico para a página inicial...
