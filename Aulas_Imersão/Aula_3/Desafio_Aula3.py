import pandas as pd
import plotly.express as px

# Função de impressão formatada
def bloco(titulo, conteudo=None):
    print(f"\n{'#'*5} {titulo.upper()} {'#'*5}\n")
    if conteudo is not None:
        print(conteudo)

# Lê o arquivo CSV
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Dicionário com os novos nomes de colunas
novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

# Renomeia as colunas
df.rename(columns=novos_nomes, inplace=True)

# Filtra apenas para o cargo "Data Science"
df_ds = df[df['cargo'] == 'Data Science']

# Calcula o salário médio por país
salario_pais = df_ds.groupby('residencia', as_index=False)['usd'].mean()

# Cria o mapa interativo
fig = px.choropleth(
    salario_pais,
    locations='residencia',        # Coluna com código do país
    locationmode='ISO-3',          # ISO Alpha-3 (ex.: BRA, USA)
    color='usd',                   # Cor baseada no salário médio
    hover_name='residencia',       # Mostra o país ao passar o mouse
    color_continuous_scale='Viridis',
    title='Salário Médio por País - Data Science (USD)'
)

# Exibe o mapa
fig.show()