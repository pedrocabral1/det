import streamlit as st
import pandas as pd

# Configuração inicial da página
st.set_page_config(
    page_title="Dashboard de Análises",
    page_icon="📊",
    layout="wide"
)

# Configuração da barra lateral
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #ECEFF1;
        color: #37474F;
        font-size: 0.6em;
    }
    .sidebar h1, .sidebar h2, .sidebar h3, .sidebar h4, .sidebar h5, .sidebar h6 {
        color: #1E88E5;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo da Unifor centralizada na barra lateral
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <img src="https://www.unifor.br/o/unifor-theme/images/unifor-logo-horizontal.svg" width="80px">
    </div>
    """,
    unsafe_allow_html=True
)

# Título dos participantes
st.sidebar.markdown(
    """
    <div style="text-align: center; color: #1E88E5; font-size: 0.7em; font-weight: bold;">Participantes do Projeto</div>
    """,
    unsafe_allow_html=True
)

# Lista de participantes
participants = {
    "Denis Neres Caminha": {
        "LinkedIn": "https://www.linkedin.com/in/denis-caminha-53ab05b6/",
        "GitHub": "https://github.com/diCaminha"
    },
    "Paulo Dario Soares Coelho": {
        "LinkedIn": "https://www.linkedin.com/in/pdariocoelho/",
        "GitHub": "https://github.com/diCaminha"
    },
    "Pedro Henrique de Araújo Cabral": {
        "LinkedIn": "https://www.linkedin.com/in/pedro-cabral-professor/",
        "GitHub": "https://github.com/pedrocabral1/det"
    },
    "Thiago Pinto Pereira": {
        "LinkedIn": "https://linkedin.com.br/in/thiagoppce",
        "GitHub": "https://github.com/thiagopintopereira"
    }
}

# Ícones de LinkedIn e GitHub
linkedin_icon = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
github_icon = "https://cdn-icons-png.flaticon.com/512/25/25231.png"

for name, links in participants.items():
    st.sidebar.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: center; font-size: 0.6em; color: #37474F; margin-bottom: 5px;">
            <span>{name}</span>
            <a href="{links['LinkedIn']}" target="_blank" style="margin-left: 5px;">
                <img src="{linkedin_icon}" width="10px" style="vertical-align: middle;"/>
            </a>
            <a href="{links['GitHub']}" target="_blank" style="margin-left: 4px;">
                <img src="{github_icon}" width="10px" style="vertical-align: middle;"/>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Link do repositório do GitHub na barra lateral
st.sidebar.markdown(
    """
    <div style="text-align: center; color: #1E88E5; font-size: 0.7em; font-weight: bold;">Links do Projeto</div>
    <div style="text-align: center;">
        <a href="https://github.com/pedrocabral1/det" target="_blank" style="font-size: 0.6em; color: #1E88E5;">Repositório no GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

# CSS para centralizar o título e ajustar o layout
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            color: #1E88E5;
            font-weight: bold;
            font-size: 2em;
            margin-bottom: 20px;
        }
        .description {
            text-align: justify;
            font-size: 0.9em;
            color: #5A5A5A;
            margin-top: -15px;
            margin-bottom: 15px;
        }
        .plot-container {
            background-color: #F8F9FA;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Função para carregar e exibir gráficos com controle deslizante
def load_and_display_chart(url, index_column, value_column, title, description):
    try:
        df = pd.read_parquet(url)
        df = df.sort_values(by=value_column, ascending=False)
        
        max_records = len(df)
        num_records = st.slider(f"Selecione a quantidade de {title} a serem exibidos", 5, max_records, 10, key=title)
        
        df_top = df.head(num_records).set_index(index_column)
        
        st.markdown("<div class='plot-container'>", unsafe_allow_html=True)
        st.subheader(title)
        st.bar_chart(df_top[value_column])
        st.markdown(f"<div class='description'>{description}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo '{url}': {e}")

# Título e introdução do dashboard
st.markdown("<h1 class='main-title'>Dashboard de Análises</h1>", unsafe_allow_html=True)
st.markdown("Explore visualizações e insights sobre os dados de terrorismo.")

# URLs para os arquivos Parquet no GitHub
file_urls = {
    'Número de Ataques por Tipo': ('https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_attacktype_pt.parquet', 'tipo_ataque', 'quantidade'),
    'Número de Ataques por País': ('https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_events_by_country_pt.parquet', 'pais', 'quantidade'),
    'Número de Mortes por Grupo': ('https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_gname_nkill_pt.parquet', 'grupo', 'soma_mortes'),
    'Número de Mortes por Ano': ('https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_iyear_nkill_pt.parquet', 'ano', 'soma_mortes'),
    'Número de Ataques Suicidas por País': ('https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_suicide_country_pt.parquet', 'pais', 'quantidade'),
    'Número de Mortes por Região': ('https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_region_nkill_pt.parquet', 'regiao', 'soma_mortes'),
    'Número de Ataques por Tipo de Arma': ('https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_weaptype_pt.parquet', 'tipo_arma', 'quantidade')
}

# Layout de colunas para distribuir os gráficos
col1, col2 = st.columns(2)

with col1:
    load_and_display_chart(
        *file_urls['Número de Ataques por Tipo'],
        'Número de Ataques por Tipo', 
        'Este gráfico mostra o número de ataques classificados por tipo, ajudando a entender os métodos mais utilizados pelos terroristas.'
    )

    load_and_display_chart(
        *file_urls['Número de Ataques por País'],
        'Número de Ataques por País', 
        'Distribuição dos ataques por país, oferecendo uma visão das regiões mais afetadas pelo terrorismo.'
    )

    load_and_display_chart(
        *file_urls['Número de Mortes por Grupo'],
        'Número de Mortes por Grupo', 
        'Mostra os grupos responsáveis pelo maior número de mortes em ataques terroristas.'
    )

with col2:
    load_and_display_chart(
        *file_urls['Número de Mortes por Ano'],
        'Número de Mortes por Ano', 
        'A evolução anual do número de mortes em ataques terroristas ao longo do tempo.'
    )

    load_and_display_chart(
        *file_urls['Número de Ataques Suicidas por País'],
        'Número de Ataques Suicidas por País', 
        'Número de ataques suicidas distribuídos por país, indicando regiões onde essa tática é mais comum.'
    )

    load_and_display_chart(
        *file_urls['Número de Mortes por Região'],
        'Número de Mortes por Região', 
        'Distribuição do número de mortes em ataques terroristas por região.'
    )

    load_and_display_chart(
        *file_urls['Número de Ataques por Tipo de Arma'],
        'Número de Ataques por Tipo de Arma', 
        'Frequência de uso de diferentes tipos de armas em ataques terroristas.'
    )
