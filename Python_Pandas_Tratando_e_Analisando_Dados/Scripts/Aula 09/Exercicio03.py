# Importando bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

# Configurando o Matplotlib
%matplotlib inline
plt.rc('figure',figsize=(20,10))

# Importando a base de Dados

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Brutos\aluguel_amostra.csv',sep=';')
dados.head()

### Criando uma series com a variavel desejada
valor = dados['Valor m2']
valor.head()

### Primeiro Quartil (25%)
Q1 = valor.quantile(.25)
Q1

### Terceiro Quartil (75%)
Q3 = valor.quantile(.75)
Q3

### Intervalo interquaril
IIQ = Q3- Q1
IIQ
### Limite inferior
limite_inferior = Q1 - 1.5*IIQ
limite_inferior
limite_superior = Q3 + 1.5*IIQ
limite_superior
