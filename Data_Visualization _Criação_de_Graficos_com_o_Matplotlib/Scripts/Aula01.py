# Capítulo 03 - Fazendo as primeiras visualizações

## Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

## Importando dados
df = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Data Visualization - Criação de Gráficos com o Matplotlib\Dados Brutos\monitoramento_tempo.csv')

## Primeiras informações
df.head()
df.info()

## Ajustes preliminares
df['data'] = pd.to_datetime(df['data'])
df.info()

## Primeiras visualizações
plt.figure(figsize=(15,8)) # Ajustear o tamanho da figura
plt.plot(df.data,df.temperatura)

## Adicionar título ao gráfico
plt.figure(figsize=(15,8)) # Ajustar o tamanho da figura
plt.plot(df.data,df.temperatura)
plt.title('Temperatura x Tempo') #Adicionar título a figura


# Capítulo 04 - Funcionalidades básicas do matplotlib
## Uma maneira de tornar a criação de gráficos mais robusta no matplotlib é a utilização de figuras. Elas nos dão maior controle sobre os elementos da figura

fig = plt.figure(figsize=(15,8)) #Cria figura
eixo = fig.add_axes([0,0,1,1]) #Adiciona um elemento de eixo

## Incuindo o gráfico similar ao que fizemos antes
fig = plt.figure(figsize=(15,8)) #Cria figura
eixo = fig.add_axes([0,0,1,1]) #Adiciona um elemento de eixo
eixo.plot(df.data,df.temperatura)
eixo.set_title('Temperatura x Data')

## Incluindo legendas dos eixos
fig = plt.figure(figsize=(15,8)) #Cria figura
eixo = fig.add_axes([0,0,1,1]) #Adiciona um elemento de eixo
eixo.plot(df.data,df.temperatura)
eixo.set_title('Temperatura x Data') # Define o título do gráfico
eixo.set_ylabel('Temperatura') # Define o titulo do eixo Y
eixo.set_xlabel('Data') # Define o titulo do eixo X

## Ajustando as legendas
### O argumento 'fontsize' pode ser utilizado para ajustar o tamanho dos elementos
fig = plt.figure(figsize=(15,8)) #Cria figura
eixo = fig.add_axes([0,0,1,1]) #Adiciona um elemento de eixo
eixo.plot(df.data,df.temperatura)
eixo.set_title('Temperatura x Data',fontsize=25) # Define o título do gráfico
eixo.set_ylabel('Temperatura',fontsize=20) # Define o titulo do eixo Y
eixo.set_xlabel('Data',fontsize=20) # Define o titulo do eixo X

## Adicionar legenda dos dados
fig = plt.figure(figsize=(15,8)) #Cria figura
eixo = fig.add_axes([0,0,1,1]) #Adiciona um elemento de eixo
eixo.plot(df.data,df.temperatura)
eixo.set_title('Temperatura x Data',fontsize=25) # Define o título do gráfico
eixo.set_ylabel('Temperatura',fontsize=20) # Define o titulo do eixo Y
eixo.set_xlabel('Data',fontsize=20) # Define o titulo do eixo X
eixo.legend(['Temperatura'],loc='lower right',fontsize=15) # Define a legenda dos dados com 'loc' determinando a posição dele dentro do eixo.

## Ajustando as cores do gráfico
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.plot(df.data,df.temperatura,color='deeppink') # O argumento 'color' recebe a cor desejada
eixo.set_title('Temperatura x Data',fontsize=25)
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)
