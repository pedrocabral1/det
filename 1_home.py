import streamlit as st
import pandas as pd

# Links para os arquivos .parquet no formato bruto no GitHub
file_urls = {
    'df_totals_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_totals_pt.parquet',
    'df_attacktype_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_attacktype_pt.parquet',
    'df_events_by_country_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_events_by_country_pt.parquet',
    'df_gname_nkill_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_gname_nkill_pt.parquet',
    'df_iyear_nkill_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_iyear_nkill_pt.parquet',
    'df_suicide_country_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_suicide_country_pt.parquet',
    'df_region_nkill_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_region_nkill_pt.parquet',
    'df_weaptype_pt': 'https://raw.githubusercontent.com/pedrocabral1/det/main/datasets/df_weaptype_pt.parquet'
}

# Carregar dados no estado da sessão
if "data" not in st.session_state:
    dfs = {name: pd.read_parquet(url) for name, url in file_urls.items()}
    st.session_state["data"] = dfs

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

# Logo da Unifor centralizada acima dos elementos
st.sidebar.markdown(
    """
    <div style="text-align: center; margin-bottom: 10px;">
        <img src="https://www.unifor.br/o/unifor-theme/images/unifor-logo-horizontal.svg" width="80px">
    </div>
    """,
    unsafe_allow_html=True
)

# Título dos participantes do projeto com menor fonte e centralizado
st.sidebar.markdown(
    """
    <div style="text-align: center; color: #1E88E5; font-size: 0.7em; font-weight: bold;">Participantes do Projeto</div>
    """,
    unsafe_allow_html=True
)

# Lista de participantes centralizada com ícones de LinkedIn e GitHub menores
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

# Link do repositório do projeto no GitHub
st.sidebar.markdown(
    """
    <div style="text-align: center; color: #1E88E5; font-size: 0.7em; font-weight: bold;">Links do Projeto</div>
    <div style="text-align: center;">
        <a href="https://github.com/pedrocabral1/det" target="_blank" style="font-size: 0.6em; color: #1E88E5;">Repositório no GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Imagem de capa - Substitua o caminho local pela URL da imagem, se disponível no GitHub
st.image("https://raw.githubusercontent.com/pedrocabral1/det/main/imagens/capa-det.webp", use_column_width=True)

# Conteúdo principal justificado
st.markdown(
    """
    <div style="text-align: justify;">
        <h1>Análise de Dados de Eventos de Terrorismo</h1>
        <p>Este projeto, desenvolvido para a disciplina <strong>Engenharia de Dados II</strong> no <strong>MBA em Ciência de Dados</strong> da <strong>Universidade de Fortaleza (Unifor)</strong>, explora a complexidade e o impacto dos eventos terroristas globais. O trabalho utiliza o <strong>Global Terrorism Database (GTD)</strong>, uma base de dados pública e abrangente mantida pelo <strong>National Consortium for the Study of Terrorism and Responses to Terrorism (START)</strong>, da <strong>University of Maryland</strong>. Essa base contém dados detalhados sobre mais de 200.000 ataques terroristas ocorridos desde 1970, cobrindo variáveis como data, local, tipo de ataque, alvos, número de vítimas e grupos responsáveis.</p>
        <p>O uso do <strong>Apache Spark</strong> possibilitou o tratamento de grandes volumes de dados em um pipeline estruturado em camadas (bronze, silver e gold), onde cada etapa inclui transformações específicas, limpeza e agregação para garantir qualidade e eficiência na análise. Este projeto não só representa uma aplicação prática dos princípios de engenharia de dados, mas também fornece insights valiosos sobre as tendências e padrões associados ao terrorismo ao longo do tempo e em diferentes regiões.</p>
        <p>A escolha da base GTD, em particular, deve-se à sua confiabilidade e riqueza de informações, que permitem análises robustas e visualizações claras para auxiliar na compreensão do fenômeno do terrorismo e na formulação de respostas informadas por dados. Este dashboard fornece visualizações interativas, permitindo que o usuário explore as características dos ataques, observe padrões e entenda a dimensão do problema em diferentes contextos geográficos e temporais.</p>
        <p>Convida-se o usuário a explorar a página de <strong>Overview dos Dados</strong> para um entendimento geral das características do dataset e, em seguida, navegar pela <strong>Página do Dashboard</strong> para visualizar as análises e insights gerados a partir desses dados.</p>
    </div>
    """,
    unsafe_allow_html=True
)
