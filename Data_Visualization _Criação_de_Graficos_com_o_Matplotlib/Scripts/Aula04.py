# Capítulo 02 - Utilizando gráficos de dispersão

## Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import datetime

## Importando dados
df = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Data Visualization - Criação de Gráficos com o Matplotlib\Dados Brutos\iris.csv')

## Primeiras informações
df.head()
df.info()

## Analises visuais preliminares - Scatterplot
fig = plt.figure(figsize=(12,6))
eixo = fig.add_axes([0,0,1,1])
eixo.scatter(df['comprimento_sépala'],df['largura_sépala'])
eixo.set_title('Gráfico de Dispersão - Sépala',fontsize=25,pad=15)
eixo.set_xlabel('Comprimento da Sépala',fontsize=15)
eixo.set_ylabel('Largura da Sépala',fontsize=15)
eixo.tick_params(labelsize=10) #Define os parametros para os ticks dos eixos

## Alterando as cores por categoria
fig = plt.figure(figsize=(12,6))
eixo = fig.add_axes([0,0,1,1])
cores = {'Iris-setosa':'deeppink','Iris-versicolor':'lightblue','Iris-virginica':'gray'} #Dicionario definindo as cores para cada espécie.
for especie in df['espécie'].unique(): #Neste caso, a partir do dicionario acima, plotamos cada uma das espécies separadamente
    tmp = df[df['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'],tmp['largura_sépala'],color = cores[especie]) # Variável 'color' recebe o dicionário definido acima
eixo.set_title('Gráfico de Dispersão - Sépala',fontsize=25,pad=15)
eixo.set_xlabel('Comprimento da Sépala',fontsize=15)
eixo.set_ylabel('Largura da Sépala',fontsize=15)
eixo.legend(cores,fontsize=15)
eixo.tick_params(labelsize=10)

## Alterando os marcadores
## Podemos alterar os marcadores para analisar visualmente se temos dois pontos no mesmo lugar, se sobreponto.
fig = plt.figure(figsize=(12,6))
eixo = fig.add_axes([0,0,1,1])
cores = {'Iris-setosa':'deeppink','Iris-versicolor':'lightblue','Iris-virginica':'gray'} #Dicionario definindo as cores para cada espécie.
marcadores = {'Iris-setosa':'x','Iris-versicolor':'o','Iris-virginica':'v'} #Dicionario para definir os marcadores para cada especie
for especie in df['espécie'].unique(): #Neste caso, a partir do dicionario acima, plotamos cada uma das espécies separadamente
    tmp = df[df['espécie'] == especie]
    eixo.scatter(tmp['comprimento_sépala'],tmp['largura_sépala'],
                    color = cores[especie],
                    marker=marcadores[especie],
                    s=100)
eixo.set_title('Gráfico de Dispersão - Sépala',fontsize=25,pad=15)
eixo.set_xlabel('Comprimento da Sépala',fontsize=15)
eixo.set_ylabel('Largura da Sépala',fontsize=15)
eixo.legend(cores,fontsize=15)
eixo.tick_params(labelsize=10)


# Capitulo 04 - Visualizando a distribuição de dados
fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])

cores = ['deeppink','lightblue','gray','deepskyblue'] #define as cores que vamos utilizar
caixas = eixo.boxplot(df.drop('espécie',axis=1),patch_artist=True) #patch_artist: Preenche os boxplots
eixo.set_title('BoxPlot',fontsize=15,pad=10)
eixo.set_xticklabels(df.drop('espécie',axis=1).columns)

#Loop para associar uma cor para cada caixa do boxplot
# caixas['boxes'] retorna cada uma das caixas do boxplot
for caixa,cor in zip(caixas['boxes'],cores):
    caixa.set(color=cor)

# Loop para alterar a visualização dos outliers

for outlier in caixas['fliers']:
    outlier.set(marker='x',markersize=6,markeredgecolor='red')
    #marker: altera o simbolo Utilizado
    #markersize: tamanho do marcador
    #markeredgecolor: cor do marcador


# Capítulo 05 - Outra forma de visualizar a distribuição de dados
## utilizando Histogramas

fig = plt.figure(figsize=(5,4))
eixo = fig.add_axes([0,0,1,1])
eixo.hist(df['comprimento_pétala'],bins=20,density=True)
#bins define a quantidade de subgrupos que os dados serão dividios
#density determina se o histograma vai ser normalizado ou não
eixo.set_title('Histograma',fontsize=15,pad=10)
eixo.set_xlabel('Comprimento da Pétala',fontsize=15)
eixo.grid(True)
