import pandas as pd

# Caminhos dos arquivos Parquet
paths = [
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_totals_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_attacktype_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_events_by_country_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_gname_nkill_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_iyear_nkill_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_suicide_country_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_region_nkill_pt.parquet",
    r"C:\Users\User\OneDrive\00-ciencias-de-dados\det\datasets\df_weaptype_pt.parquet"
]

# Carregar e exibir cada DataFrame
for path in paths:
    df = pd.read_parquet(path)
    print(f"Visualizando o DataFrame para: {path.split('\\')[-1]}")
    print(df.head(), "\n")  # Mostra as primeiras linhas de cada DataFrame