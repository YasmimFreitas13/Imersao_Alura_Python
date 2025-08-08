import pandas as pd
import plotly.express as px
import pycountry

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
    'salary_in_usd': 'usd',  # <- aqui o nome será 'usd'
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

# Renomeia as colunas
df.rename(columns=novos_nomes, inplace=True)

# Cria um DataFrame limpo para manipulação
df_limpo = df.copy()

# Função para converter ISO-2 para ISO-3
def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None

# Criar nova coluna com código ISO-3
df_limpo['residencia_iso3'] = df_limpo['residencia'].apply(iso2_to_iso3)

# Calcular média salarial por país (apenas Data Scientist)
ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
media_ds_pais = ds.groupby('residencia_iso3')['usd'].mean().reset_index()

# Gerar o mapa
fig = px.choropleth(
    media_ds_pais,
    locations='residencia_iso3',
    color='usd',
    color_continuous_scale='rdylgn',
    title='Salário médio de Cientista de Dados por país',
    labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
)

fig.show()