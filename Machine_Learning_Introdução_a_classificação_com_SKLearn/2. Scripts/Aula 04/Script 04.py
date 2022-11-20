# Aula 04

## Atualização do modelo SVC


### O linearSVC encontra relações lineares e como pudemos ver nos nossos dados, parece não existir uma relação linear

import pandas as pd

uri = 'https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv'

dados = pd.read_csv(uri)
dados.head()

### Nossos dados consistem em três colunas: unifinished -> Se o projeto foi concluido ou não; expected_hours -> Quantidade de horas esperadas para conclusão deste projeto; price -> preço ofertado para conclusão deste projeto.

### Temos Unifished (1) e finished (0). Vamos trocar estes valores para ficar mais natural a compreensão dos dados
trocar = {
    0:1,
    1:0
}
dados['finished'] = dados.unfinished.map(trocar)
dados.head()


x = dados[['expected_hours','price']]
y = dados['finished']

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

SEED = 20
np.random.seed(SEED)
training_x,test_x,training_y,test_y = train_test_split(x,y, random_state = SEED, test_size = 0.25, stratify = y)
print('Treinaremos com %d elementos e testaremos com %d elementos' % (len(training_x),len(test_x)))
model = SVC()
model.fit(training_x, training_y)
previsoes = model.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))

## Vamos Plotar os resultados obtidos pelo nosso novo modelo

x_min = test_x.expected_hours.min()
x_max = test_x.expected_hours.max()
y_min = test_x.price.min()
y_max = test_x.price.max()
print(x_min,x_max,y_min,y_max)

### Aqui, vamos criar nosso grid de pontos com uns códigos muito doidos do numpy.
pixels = 100
eixo_x = np.arange(x_min,x_max,(x_max-x_min)/pixels)
eixo_y = np.arange(y_min,y_max,(y_max-y_min)/pixels)
xx, yy = np.meshgrid(eixo_x,eixo_y)
pontos = np.c_[xx.ravel(),yy.ravel()]
pontos
Z = model.predict(pontos)
Z.shape #Aqui, note que temos uma lista com 10000 linhas e nosso interesse, na verdade, é em uma matriz 100x100 de valores. Para isso, vamos utilizar o reshape.
Z = Z.reshape(xx.shape)
Z.shape

import matplotlib.pyplot as plt

plt.contourf(xx,yy,Z,alpha=0.3)
plt.scatter(test_x.expected_hours,test_x.price,c=test_y, s=1)

## Nesse caso, encontramos valores distintos, mas uma caracteristica deste algoritmos é a influencia da escla das features. Para isso, vamos normalizar os dados utilizando uma propriedade do sklearn

from sklearn.preprocessing import StandardScaler

## Vamos criar uma escala nova para as features de x

scaler = StandardScaler()
scaler.fit(training_x) # Baseado nas features, o modelo vai aprender como normalizar os dados
## Normalizamos as features baseados na nova medida
s_training_x = scaler.transform(training_x)
s_test_x = scaler.transform(test_x)

model = SVC()
model.fit(s_training_x, training_y)
previsoes = model.predict(s_test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))

## Antes de plotar os nossos resultados, note que nossos dados mudaram de forma, antes era um dataframe e agora é um array
training_x
s_training_x

# Vamos Plotar os resultados obtidos pelo nosso novo modelo. Para isso, vamos fazer alguns ajustes aos dados

data_x = s_test_x[:,0]
data_y = s_test_x[:,1]
x_min = data_x.min()
x_max = data_x.max()
y_min = data_y.min()
y_max = data_y.max()
print(x_min,x_max,y_min,y_max)

### Aqui, vamos criar nosso grid de pontos com uns códigos muito doidos do numpy.
pixels = 100
eixo_x = np.arange(x_min,x_max,(x_max-x_min)/pixels)
eixo_y = np.arange(y_min,y_max,(y_max-y_min)/pixels)
xx, yy = np.meshgrid(eixo_x,eixo_y)
pontos = np.c_[xx.ravel(),yy.ravel()]
pontos
Z = model.predict(pontos)
Z.shape #Aqui, note que temos uma lista com 10000 linhas e nosso interesse, na verdade, é em uma matriz 100x100 de valores. Para isso, vamos utilizar o reshape.
Z = Z.reshape(xx.shape)
Z.shape

import matplotlib.pyplot as plt

plt.contourf(xx,yy,Z,alpha=0.3)
plt.scatter(data_x,data_y,c=test_y, s=1)
