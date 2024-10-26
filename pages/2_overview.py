import streamlit as st
import pandas as pd

# Configuração inicial da página
st.set_page_config(
    page_title="Overview dos Dados",
    page_icon="📊",
    layout="centered"
)

# CSS para centralizar o título e ajustar a tabela
st.markdown(
    """
    <style>
        /* Centralizar o título e aplicar cor */
        .main-title {
            text-align: center;
            color: #37474F; /* Cor do título da Home */
            font-weight: bold;
            font-size: 2em;
            margin-bottom: 20px;
        }
        
        /* Ajustar largura da descrição */
        .description {
            max-width: 800px;
            margin: auto;
            text-align: justify;
        }
        
        /* Centralizar a tabela */
        .table-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Configuração da barra lateral
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

# Ícones menores para LinkedIn e GitHub centralizados
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

# Link do repositório do projeto no GitHub com menor fonte e centralizado
st.sidebar.markdown(
    """
    <div style="text-align: center; color: #1E88E5; font-size: 0.7em; font-weight: bold;">Links do Projeto</div>
    <div style="text-align: center;">
        <a href="https://github.com/pedrocabral1/det" target="_blank" style="font-size: 0.6em; color: #1E88E5;">Repositório no GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Carregar os dados do arquivo Parquet
file_path = r'C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_totals_pt.parquet'
df_totals = pd.read_parquet(file_path)

# Título centralizado
st.markdown("<h1 class='main-title'>Overview dos Dados</h1>", unsafe_allow_html=True)

# Descrição centralizada com largura ajustada
st.markdown(
    """
    <div class="description">
        Esta tabela exibe um resumo dos conjuntos de dados disponíveis para análise, incluindo o nome de cada DataFrame e a quantidade total de registros.
        Cada quadro de dados representa uma coleção específica de informações sobre eventos terroristas, como o número de ataques por país, tipos de ataques, 
        número de mortes por ano e muito mais.
    </div>
    """,
    unsafe_allow_html=True
)

# Explicações de cada coluna
explicacoes = {
    "df_events_by_country": "Número total de eventos terroristas por país.",
    "df_attacktype": "Tipos de ataque registrados nos eventos terroristas.",
    "df_iyear_nkill": "Número de mortes por ano em eventos terroristas.",
    "df_weaptype": "Tipos de armas utilizadas nos ataques.",
    "df_suicide_country": "Ataques suicidas classificados por país.",
    "df_region_nkill": "Número de mortes por região.",
    "df_gname_nkill": "Grupos responsáveis e número de mortes associadas."
}

df_totals.columns = ["Quadro de Dados", "Total de Registros"]
df_totals["Descrição"] = df_totals["Quadro de Dados"].map(explicacoes)

# Exibir a tabela centralizada com a barra de progresso
st.markdown('<div class="table-container">', unsafe_allow_html=True)
st.dataframe(
    df_totals,
    column_config={
        "Total de Registros": st.column_config.ProgressColumn(
            "Total de Registros", format="%d", min_value=0, max_value=df_totals["Total de Registros"].max()
        )
    }
)
st.markdown('</div>', unsafe_allow_html=True)
