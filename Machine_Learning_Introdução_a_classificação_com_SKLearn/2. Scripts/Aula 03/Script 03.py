# Aula 03

## Testando em duas dimensões

### Neste projeto, vamos trabalhar com dados referente à contratação de um profissional para criação de uma página web.

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

### Note que neste caso, temos duas features (Expected Hours e Price) e duas classes (unfinished e finished)
### Neste caso, podemos desenhar em eixos coordenados as duas features.

import seaborn as sns

sns.scatterplot(x='expected_hours',y='price',data=dados)

### No gráfico acima, temos todos os projetos plotados com expected_hours no eixo X e price no eixo y. Porém, não há distinção entre projetos concluidos e não concluidos.
### Para resolver este problema, podemos utilizar um argumento adicional do seaborn

sns.scatterplot(x='expected_hours',y='price',hue='finished',data=dados)

### Podemos ainda, utilizar dois gráficos distintos, utilizando relplot ao invés do scatterplot e adicionando o argumento 'col'.
sns.relplot(x='expected_hours',y='price',hue='finished',col='finished',data=dados)


### Agora, vamos partir para o modelo de classificação.

x = dados[['expected_hours','price']]
y = dados['finished']

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

SEED = 20
np.random.seed(SEED)
training_x,test_x,training_y,test_y = train_test_split(x,y, random_state = SEED, test_size = 0.25, stratify = y)
print('Treinaremos com %d elementos e testaremos com %d elementos' % (len(training_x),len(test_x)))
model = LinearSVC()
model.fit(training_x, training_y)
previsoes = model.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))

### Neste caso, não conseguimos avalisar se nosso modelo preditivo é bom ou ruim uma vez que não temos parametros para avaliá-lo
### Para resolver este problema, vamos criar um 'teste base' (baseline) para que possamos avaliar. Neste, vamos supor que nosso projeto é sempre concluido, ou seja, finished = 1 e vamos avaliar nosso modelo com essa predição

import numpy as np
baseline = np.ones(len(test_x))
acuracia_baseline = accuracy_score(test_y,baseline)
print("A acurácia baseline é de %.2f%%" % (acuracia_baseline*100))

### Como podemos ver, nosso modelo conseguiu ser pior (dado o seed considerado e a aleatoriedade envolvida) pior do que assumir que todos os projetos foram concluidos.
### Isto nos mostra que durante nem sempre, o resultado obtido inicialmente é bom ou ideal.

## Curva de Decisão
 sns.scatterplot(x='expected_hours',y='price',hue=test_y,data=test_x)
### No sctter plot acima, temos os dados referentes ao conjunto de teste e com a cor baseada na classe dos elementos de teste. Podemos ver que nossos dados de teste estão bem distribuidos

### O proximo passo é, então, tentar rodar cada um dos possíves valores das features no modelo e ver qual a sua interpretação. Depois disso, podemos plotar estes pontos baseados nas suas cores

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
