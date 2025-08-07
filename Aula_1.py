#Aula 1 - Análise de Dados com Pandas

import pandas as pd

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

# Dicionários para traduzir as categorias
senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}

contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M': 'media'
}

mapa_trabalho = {
    0: 'presencial',
    50: 'hibrido',
    100: 'remoto'
}

# Substitui as siglas pelas descrições
df['senioridade'] = df['senioridade'].replace(senioridade)
df['contrato'] = df['contrato'].replace(contrato)
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['remoto'] = df['remoto'].replace(mapa_trabalho)

# Exibição organizada
bloco("Primeiras linhas do DataFrame", df.head().to_string())

bloco("Informações do DataFrame")
print(df.info())

bloco("Estatísticas descritivas numéricas", df.describe())

bloco("Estatísticas descritivas categóricas", df.describe(include='object'))

bloco("Dimensão do DataFrame (linhas, colunas)", df.shape)

bloco("Nomes das colunas", df.columns)

bloco("Senioridade", df['senioridade'].value_counts())
bloco("Contrato", df['contrato'].value_counts())
bloco("Remoto", df['remoto'].value_counts())
bloco("Tamanho da empresa", df['tamanho_empresa'].value_counts())



