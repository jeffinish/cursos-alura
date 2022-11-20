# Capítulo 02 - Linhas de Restrição e anotações

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

## Utilizando limitações dos valores
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.grid(True)
eixo.plot(df['data'],df['temperatura'],color = 'deeppink')
eixo.set_title('Temperatura x Data',fontsize=25,pad=20) #O argumento pad define o espaço entre o título e gráfico
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)
eixo.axhline(max(df['temperatura']),color = 'black',linestyle='--') #Adiciona uma linha horizontal no maior valor observado na temperatura
eixo.axhline(min(df['temperatura']),color = 'black',linestyle='--') #Adiciona uma linha horizontal no maior valor observado na temperatura
x1 = df['data'][df['temperatura'].idxmax()] #Retorna o índice que apresenta o maior valor para aquela coluna
y1 = max(df['temperatura']) #Retorna o maior o valor para aquela coluna
eixo.annotate("Máxima",xy=(x1,y1),fontsize=15) # Inclui uma anotação na posição determinada pelas coordenadas do parâmetro xy;

#Capitulo 03 - Mais anotações e setas
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.grid(True)
eixo.plot(df['data'],df['temperatura'],color = 'deeppink')
eixo.set_title('Temperatura x Data',fontsize=25,pad=20) #O argumento pad define o espaço entre o título e gráfico
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)
eixo.axhline(max(df['temperatura']),color = 'black',linestyle='--') #Adiciona uma linha horizontal no maior valor observado na temperatura
eixo.axhline(min(df['temperatura']),color = 'black',linestyle='--') #Adiciona uma linha horizontal no maior valor observado na temperatura
x1 = df['data'][df['temperatura'].idxmax()] #Retorna o índice que apresenta o maior valor para aquela coluna, será utilizado para ser o final de uma seta
y1 = max(df['temperatura']) #Retorna o maior o valor para aquela coluna, será utilizado para ser o final de uma seta.
x2 = df['data'][df['temperatura'].idxmax() - 7000] #Define outro ponto para incluirmos o texto, em uma posição um pouco mais agradável
y2 = max(df['temperatura'])-5 #Define outro ponto para incluirmos o texto, em uma posição um pouco mais agradável
eixo.annotate("Máxima",xy=(x1,y1),fontsize=15,
                        xytext=(x2,y2),arrowprops=dict(facecolor='black')) # Inclui uma anotação na posição determinada pelas coordenadas do parâmetro xy; Inclui também uma seta partindo do texto até a posição indicada.

## Ajustando as setas
fig = plt.figure(figsize=(15,8))
eixo = fig.add_axes([0,0,1,1])
eixo.grid(True)
eixo.plot(df['data'],df['temperatura'],color = 'deeppink')
eixo.set_title('Temperatura x Data',fontsize=25,pad=20) #O argumento pad define o espaço entre o título e gráfico
eixo.set_ylabel('Temperatura',fontsize=20)
eixo.set_xlabel('Data',fontsize=20)
eixo.legend(['Temperatura'],loc='lower right',fontsize=15)
eixo.axhline(max(df['temperatura']),color = 'black',linestyle='--') #Adiciona uma linha horizontal no maior valor observado na temperatura
eixo.axhline(min(df['temperatura']),color = 'black',linestyle='--') #Adiciona uma linha horizontal no maior valor observado na temperatura
x1_max = df['data'][df['temperatura'].idxmax()] #Retorna o índice que apresenta o maior valor para aquela coluna, será utilizado para ser o final de uma seta
y1_max = max(df['temperatura']) #Retorna o maior o valor para aquela coluna, será utilizado para ser o final de uma seta.
x2_max = df['data'][df['temperatura'].idxmax() - 7000] #Define outro ponto para incluirmos o texto, em uma posição um pouco mais agradável
y2_max = max(df['temperatura'])-5 #Define outro ponto para incluirmos o texto, em uma posição um pouco mais agradável
eixo.annotate("Máximo",xy=(x1_max,y1_max),fontsize=15,
                        xytext=(x2_max,y2_max),arrowprops=dict(facecolor='black')) # Inclui uma anotação na posição determinada pelas coordenadas do parâmetro xy; Inclui também uma seta partindo do texto até a posição indicada.
x1_min = df['data'][df['temperatura'].idxmin()] #Retorna o índice que apresenta o maior valor para aquela coluna, será utilizado para ser o final de uma seta
y1_min = min(df['temperatura']) #Retorna o maior o valor para aquela coluna, será utilizado para ser o final de uma seta.
x2_min = df['data'][df['temperatura'].idxmin() - 7000] #Define outro ponto para incluirmos o texto, em uma posição um pouco mais agradável
y2_min = min(df['temperatura'])+5 #Define outro ponto para incluirmos o texto, em uma posição um pouco mais agradável
eixo.annotate("Mínimo",xy=(x1_min,y1_min),fontsize=15,
                        xytext=(x2_min,y2_min),arrowprops=dict(facecolor='black')) # Inclui uma anotação na posição determinada pelas coordenadas do parâmetro xy; Inclui também uma seta partindo do texto até a posição indicada.


# Capítulo 05 - Algumas outras visualizações
## Criando um gráfico com a média de temperatura por dia da semana
temperatura_por_dia_da_semana = df.groupby('dia_da_semana')['temperatura'].mean()
order = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado'] #Ordenando os dias manuamente
temperatura_por_dia_da_semana = temperatura_por_dia_da_semana[order]
temperatura_por_dia_da_semana
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])
indice = range(len(temperatura_por_dia_da_semana))
cores = ['black','red','deeppink','lightblue','orange','magenta','grey'] #Define uma cor para cara bara
eixo.bar(indice,temperatura_por_dia_da_semana,color=cores,edgecolor='black') # O variável 'color' recebe uma cor uma array de cores para o gráfico de barras; edgecolor define uma cor para o contorno para as barras
eixo.set_title('Temperatura média por dia da Semana',fontsize=15,pad=10)
eixo.set_xlabel('Dia da Semana',fontsize=15)
eixo.set_ylabel('Temperatura Média',fontsize=15)
eixo.set_xticks(indice)
eixo.set_xticklabels(order) #Define qual o texto que vai ser apresentado em cada Tick

## Experimentando com gráficos de pizzas
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])
explodir = [0.1,0,0,0,0,0.1,0.1] #Define quais índices (através da posição na array) serão explodidos e o quanto serão deslocados (através do valor percentual)
eixo.pie(temperatura_por_dia_da_semana,labels=temperatura_por_dia_da_semana.index,
            autopct='%.1f%%',explode=explodir,shadow=True) # O gráfico de pizza precisa receber os valores e os Labels para aqueles valores, por isso incluimos a variável 'labels'. 'Autopct' inclui o percentual dos valores por parcela; 'Explode' separada as fatias determinadas pela array; 'shadows' inclui sombras 
eixo.set_title('Temperatura média por dia da Semana',fontsize=15,pad=10)
