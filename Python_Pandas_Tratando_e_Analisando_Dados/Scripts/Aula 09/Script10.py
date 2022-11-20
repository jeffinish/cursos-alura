# Importando bibliotecas

import pandas as pd
import matplotlib.pyplot as plt

# Configurando o Matplotlib
%matplotlib inline
plt.rc('figure',figsize=(20,10))

# Importando a base de Dados

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial_m2.csv',sep=';')
dados.head()
## Capítulo 02 - Identificando e removendo Outliers

### Vamos utilizar o grafico BoxPlot para visualizar os outliers

dados.boxplot(['Valor'])

### Vamos visualizar os dados que estão muitos discrepantes
 dados[dados.Valor >= 500000]

### Para facilitar nossa vida, vamos criar uma Series para trabalhar
 valor = dados.Valor

 ### Vamos trabalhar agora para calcular os valores necessários para produzir o boxplot
 ### Primeiro Quartil (25%)
Q1 = valor.quantile(.25)
Q1

### Terceiro Quartil (75%)
Q3 = valor.quantile(.75)
Q3

### Intervalo interquaril
IIQ = Q3- Q1

### Limite inferior
limite_inferior = Q1 - 1.5*IIQ
limite_superior = Q3 + 1.5*IIQ


### Vamos filtrar apenas os valores que estão dentro dos limites
selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]
dados_new.boxplot(['Valor'])


### Podemos ver também a distribuição dos valores
dados_new.hist(['Valor'])
### Note que se fizermos a mesma coisa com os dados originais, temos um histograma muito Feio
dados.hist(['Valor'])


## Capitulo 4 - Identificando e Removendo Outlierts por Grupo

### Podemos criar o boxplot dividido por grupo para melhor visualizar os dados
dados.boxplot(['Valor'],by=['Tipo'])


### Vamos criar um grupo apenas com a variável Valor
grupo_tipo = dados.groupby('Tipo')['Valor']
### Note que agora, temos uma series com os valores para cada tipo de apartamento
Q1 = grupo_tipo.quantile(.25)
Q1

### Terceiro Quartil (75%)
Q3 = grupo_tipo.quantile(.75)
Q3

### Intervalo interquaril
IIQ = Q3- Q1

### Limite inferior
limite_inferior = Q1 - 1.5*IIQ
limite_superior = Q3 + 1.5*IIQ

### Agora, vamos fazer a remoção dos outliers com um loop for
### Obs.: Para vermos apenas as chaves do grupoby, utilizamos o método groups.keys()

dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados.Valor >= limite_inferior[tipo]) & (dados.Valor <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new,dados_selecao])

dados_new.boxplot(['Valor'],by=['Tipo'])

dados_new.to_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_sem_outliers.csv',sep=';',index=False)

## Capítulo 06 - (Extra) Mais sobre gráficos
dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_sem_outliers.csv',sep=';')

area = plt.figure()
g1 = area.add_subplot(2,2,1)
g2 = area.add_subplot(2,2,2)
g3 = area.add_subplot(2,2,3)
g4 = area.add_subplot(2,2,4)

g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor x Area')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100)
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra Valor')

grupo = dados.groupby('Tipo')['Valor']
g4.bar(grupo.mean().index,grupo.mean().values)
g4.set_title('Valor Médio por Tipo')
area
area.savefig('grafico.png',dpi=300,bbox_inches='tight')
