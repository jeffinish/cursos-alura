# Capítulo 05 - Trabalhando com dados

import pandas as pd
## Para editar a quantidade de linhas e colunas apresentados no notebook
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',1000)

dataset = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python para Data Science - Funções, Pacotes e Pandas Básico\Dados Brutos\db.csv',sep=';')
dataset

## Para vermos quais são os tipos de dados em cada uma das colunas, utilizamos o método dtypes
dataset.dtypes

## Para obtermos, de maneira rápid algumas estatísticas descritivas (de colunas que fazerem sentido) podemos utilizar o método 'describe'

dataset[['Quilometragem','Valor']].describe()

## Para obtermos uma visão geral do conjunto de dados, podemos utilizar o método 'info'
dataset.info()
