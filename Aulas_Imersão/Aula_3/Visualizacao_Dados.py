# Aula 3 - Visualização de Dados

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

# Mapeando os códigos de senioridade para nomes mais descritivos
mapeamento_senioridade = {
    'EN': 'junior',
    'MI': 'pleno',
    'SE': 'senior',
    'EX': 'executivo'
}
df['senioridade'] = df['senioridade'].map(mapeamento_senioridade)


# Verifica e remove dados nulos
df_limpo = df.dropna()

# Gráfico de barras para distribuição de senioridade
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y='usd')
plt.title("Salário Médio por Nível de Senioridade")
plt.xlabel("Nível de Senioridade")
plt.ylabel("Salário em USD")
plt.show()

# Gráfico de histograma
plt.figure(figsize=(10,5))
sns.histplot(df_limpo['usd'], bins=50, kde=True)
plt.title("Distribuição dos Salários Anuais")
plt.xlabel("Salário em USD")
plt.ylabel("Frequência")
plt.show()

# Boxplot simples
plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['usd'])
plt.title("Boxplot Salário")
plt.xlabel("Salário em USD")
plt.show()

# Verifique as categorias únicas na coluna 'senioridade'
categorias_unicas = df_limpo['senioridade'].unique()
print("Categorias únicas de senioridade:", categorias_unicas)

# Defina a ordem de senioridade
ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']

# Ajuste a ordem para incluir apenas categorias presentes
ordem_senioridade = [nivel for nivel in ordem_senioridade if nivel in categorias_unicas]
print("Ordem de senioridade ajustada:", ordem_senioridade)

# Boxplot por senioridade
plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
plt.title("Boxplot da Distribuição por Senioridade")
plt.xlabel("Nível de Senioridade")
plt.ylabel("Salário em USD")
plt.show()

# Boxplot com paleta de cores
plt.figure(figsize=(8,5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
plt.title("Boxplot da Distribuição por Senioridade com Cores")
plt.xlabel("Nível de Senioridade")
plt.ylabel("Salário em USD")
plt.show()

# Gráfico de média salarial por senioridade usando Plotly
senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()
fig = px.bar(senioridade_media_salario,
             x='senioridade',
             y='usd',
             title='Média Salarial por Senioridade',
             labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})
fig.show()

# Gráfico de pizza para proporção dos tipos de trabalho (remoto)
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos Tipos de Trabalho')
fig.show()

df_limpo.to_csv('dados-imersao-final.csv', index=False)
