import streamlit as st
import pandas as pd

# Configuração inicial da página
st.set_page_config(
    page_title="Overview dos Dados",
    page_icon="📈",
    layout="wide"
)

# Links para os arquivos .parquet no formato bruto
file_urls = {
    'df_attacktype_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_attacktype_pt.parquet',
    # outros arquivos que serão carregados para overview
}

# Função para carregar dados de uma URL
def load_data(url):
    return pd.read_parquet(url)

# Carregar dados específicos para a página de overview
df_attacktype = load_data(file_urls['df_attacktype_pt'])

# Título e introdução
st.title("Overview dos Dados")
st.markdown("Exploração detalhada dos tipos de ataque e suas características.")

# Exibição de tabela e gráficos específicos para overview
st.subheader("Número de Ataques por Tipo")
st.bar_chart(df_attacktype.set_index("tipo_ataque")["quantidade"])

# Continuação do conteúdo específico para a página de overview...
