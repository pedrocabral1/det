import pandas as pd

# Caminhos dos arquivos Parquet originais e traduzidos
original_paths = [
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_totals.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_attacktype.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_events_by_country.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_gname_nkill.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_iyear_nkill.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_suicide_country.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_region_nkill.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_weaptype.parquet"
]

# Caminhos para salvar os arquivos traduzidos
translated_paths = [
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_totals_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_attacktype_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_events_by_country_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_gname_nkill_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_iyear_nkill_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_suicide_country_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_region_nkill_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_weaptype_pt.parquet"
]

# Dicionário de tradução de colunas
translations = {
    "dataframe": "quadro_de_dados",
    "total": "total",
    "attacktype1_txt": "tipo_ataque",
    "count": "quantidade",
    "country_txt": "pais",
    "gname": "grupo",
    "sum(nkill)": "soma_mortes",
    "iyear": "ano",
    "region_txt": "regiao",
    "weaptype1_txt": "tipo_arma"
}

# Traduz e salva cada arquivo em um novo caminho
for original, translated in zip(original_paths, translated_paths):
    df = pd.read_parquet(original)
    
    # Traduzir as colunas usando o dicionário de traduções
    df.rename(columns=translations, inplace=True)
    
    # Salva o DataFrame traduzido no novo arquivo
    df.to_parquet(translated)
    
    print(f"Arquivo traduzido salvo em: {translated}")
