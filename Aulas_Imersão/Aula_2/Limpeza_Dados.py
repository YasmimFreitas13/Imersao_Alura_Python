# Aula 2 - Limpeza de Dados com Pandas

import pandas as pd
import numpy as np

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

# Verifica dados nulos
bloco("Dados Nulos", df.isnull().sum())

# Exibe as linhas com dados nulos
bloco("Linhas com Dados Nulos", df[df.isnull().any(axis=1)])

# Exclui linhas com dados nulos
df_limpo = df.dropna()

# Verifica se os dados nulos foram removidos
bloco("Dados Nulos Após Limpeza", df_limpo.isnull().sum())

# Converte o tipo da coluna 'ano' para inteiro
df_limpo['ano'] = df_limpo['ano'].astype(int)

# Exibe as primeiras linhas do DataFrame limpo
bloco("Primeiras linhas do DataFrame Limpo", df_limpo.head().to_string())

# Exibe informações do DataFrame limpo
bloco("Informações do DataFrame Limpo")
print(df_limpo.info())

# Criação de um dataframe de teste para usar de exemplo
df_salarios = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
})

# Calcula a média salarial e substitui os nulos pela média e arredonda os valores
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

bloco("DataFrame de Salários com Média", df_salarios)

# Calcula mediana e substitui os nulos pela mediana
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

bloco("DataFrame de Salários com Mediana", df_salarios)

# DataFrame de temperaturas
df_temperaturas = pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})

df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()
bloco("DataFrame de Temperaturas com Preenchimento Forward Fill", df_temperaturas)

# DataFrame de temperaturas com Backward Fill
f_temperaturas = pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})

f_temperaturas["preenchido_bfill"] = f_temperaturas["Temperatura"].bfill()
bloco("DataFrame de Temperaturas com Preenchimento Backward Fill", f_temperaturas)

# DataFrame de cidades
df_cidades = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    'cidade': ["São Paulo", np.nan, "Curitiba", np.nan, "Belém"]
})

df_cidades['cidade_preenchida'] = df_cidades["cidade"].fillna("Não informado")
bloco("DataFrame de Cidades com Preenchimento", df_cidades)

