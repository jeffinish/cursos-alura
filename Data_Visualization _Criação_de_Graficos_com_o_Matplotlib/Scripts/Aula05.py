# Capítulo 02 - Adicionando anotações e linhas horizontais

## Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import datetime

## Importando dados
df = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Data Visualization - Criação de Gráficos com o Matplotlib\Dados Brutos\iris.csv')


fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

mu, sigma = df['comprimento_pétala'].mean(),df['comprimento_pétala'].std()
eixo.hist(df['comprimento_pétala'],bins=20)
eixo.set_title('Histograma',fontsize=15,pad=10)
eixo.set_xlabel('Comprimento da Pétala',fontsize=15)
eixo.grid(True)
eixo.annotate('$\mu = {0:.2f}$ \n $\sigma = {1:.2f}$'.format(mu,sigma),xy=(4.5,20),fontsize=20)
eixo.axvline(mu,color='deeppink',linestyle='--')
eixo.annotate('Media',xy=(mu-1.3,28),fontsize=20)
eixo.axvline(df['comprimento_pétala'].median(),color='deepskyblue',linestyle='--')
eixo.annotate('Mediana',xy=(df['comprimento_pétala'].median(),31),fontsize=20)


# Capítulo 03 - Combinando e salvando figuras

fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

mu, sigma = df['comprimento_pétala'].mean(),df['comprimento_pétala'].std()
eixo.hist(df['comprimento_pétala'],bins=20)
eixo.set_title('Histograma',fontsize=15,pad=10)
eixo.set_xlabel('Comprimento da Pétala',fontsize=15)
eixo.grid(True)
eixo.annotate('$\mu = {0:.2f}$ \n $\sigma = {1:.2f}$'.format(mu,sigma),xy=(4.5,20),fontsize=20)
eixo.axvline(mu,color='deeppink',linestyle='--')
eixo.annotate('Media',xy=(mu-1.3,28),fontsize=20)
eixo.axvline(df['comprimento_pétala'].median(),color='deepskyblue',linestyle='--')
eixo.annotate('Mediana',xy=(df['comprimento_pétala'].median(),31),fontsize=20)
