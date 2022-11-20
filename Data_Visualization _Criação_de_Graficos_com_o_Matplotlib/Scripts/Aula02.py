# Capítulo 03 - Espessura, estilo, foco, marcadores e grades

## Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import datetime

## Importando dados
df = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Data Visualization - Criação de Gráficos com o Matplotlib\Dados Brutos\monitoramento_tempo.csv')

## Primeiras informações
df.head()
df.info()

## Ajustes preliminares
df['data'] = pd.to_datetime(df['data'])
df.info()

## Ajustando a expessura do gráfico
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(df.data,df.temperatura,color='deeppink', lw = 0.3) #O argumento lw recebe o valor da Espessura do gráfico
eixo.set_title('Temperatura x Data',fontsize=25)
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)

## Ajustando o estilo da linha
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(df.data,df.temperatura,color='deeppink', ls = 'dotted') #O argumento ls recebe o estilo da linha do gráfico
eixo.set_title('Temperatura x Data',fontsize=25)
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)

## Limitando os valores a serem plotados
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(df.data,df.temperatura,color='deeppink')
eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1)) # O metodo set_xlim limita os valores do eixo x que serão plotados
eixo.set_title('Temperatura x Data',fontsize=25)
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)

## Adicionando marcadores
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(df.data,df.temperatura,color='deeppink',marker='o') #O argumento marker mostra um valor em cada ponto do gráfico
eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.set_title('Temperatura x Data',fontsize=25)
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)

## Adicionando grade
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(df.data,df.temperatura,color='deeppink')
eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.set_title('Temperatura x Data',fontsize=25)
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)
eixo.grid(True)

# Capitulo 03 - Mais de um eixo na mesma visualização
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.7,0.6,0.3,0.3])
eixo.grid(True)
eixo.plot(df['data'],df['temperatura'],color = 'deeppink')
eixo.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1))
eixo.set_title('Temperatura x Data em 2014',fontsize=25,pad=20) #O argumento pad define o espaço entre o título e gráfico
eixo.legend(['Temperatura'],loc='best',fontsize=15) #O valor 'best' faz com que o matplotlib decida onde é o melhor lugar para a legenda
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo2.grid(True)
eixo2.plot(df['data'],df['temperatura'],color = 'lightblue')
eixo2.set_title('Temperatura x Data',fontsize=15)
eixo2.legend(['Temperatura'],loc='best',fontsize=8)
eixo2.set_ylabel('Temperatura',fontsize=10)
eixo2.set_xlabel('Data',fontsize=10)

# Capítulo 04 - Uma visualização mais complexa
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo2 = fig.add_axes([0.7,0.6,0.3,0.3])
eixo.grid(True)
eixo.plot(df['data'],df['temperatura'],color = 'deeppink')
eixo.set_xlim(datetime.datetime(2014,5,1),datetime.datetime(2014,6,1)) #O gráfico principal agora exibe apenas os valores de Maio de 2014
eixo.set_ylim(270,330) # Ajusta o limite do eixo y para que os gráficos não se sobreponham
eixo.set_title('Temperatura x Data em Maio de 2014',fontsize=25,pad=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo2.grid(True)
azul_esquerda = df['data'] < datetime.datetime(2014,5,1) #Criando um filtro para podermos mudar o a cor do mes de Maio no gráfico auxiliar
azul_direita = df['data'] > datetime.datetime(2014,6,1) #Criando um filtro para podermos mudar o a cor do mes de Maio no gráfico auxiliar
rosa = (df['data'] > datetime.datetime(2014,5,1)) & (df['data'] < datetime.datetime(2014,6,1)) #Filtro para plotar apenas o período de Maio em Rosa
eixo2.plot(df[rosa]['data'],df[rosa]['temperatura'],color = 'deeppink') #Ajustando a cor do gráfico auxliar para ser a mesma do gráfico principal
eixo2.plot(df[azul_esquerda]['data'],df[azul_esquerda]['temperatura'],color='lightblue') #Criando um gráfico para sobrepor os gráfico auxiliar no período anterior a Maio
eixo2.plot(df[azul_direita]['data'],df[azul_direita]['temperatura'],color='lightblue') #Criando um gráfico para sobrepor os gráfico auxiliar no período posterior a Maio
eixo2.set_xlim(datetime.datetime(2014,1,1),datetime.datetime(2015,1,1)) #O gráfico auxiliar agora exibe apenas os valores do ano de de 2014
eixo2.set_title('Temperatura x Data em 2014',fontsize=15) 
eixo2.legend(['Temperatura'],loc='best',fontsize=8)
eixo2.set_ylabel('Temperatura',fontsize=10)
eixo2.set_xlabel('Data',fontsize=10)
