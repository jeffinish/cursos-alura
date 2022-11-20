# Aula 02

## Lendo dados da internet e manipulando os mesmos
## Neste projeto, vamos trabalhar com uma fonte de dados referente ao acesso de usuários em uma página web.
## Temos se este usuário visitou ou não quatro páginas.

import pandas as pd

uri = 'https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv'

dados = pd.read_csv(uri)
dados.head()

## Temos 3 páginas: Home, How it Works, Contact e se o cliente realizou uma compra ou não Bought.
## Estas features são: Visitou/Realizou compra (1); Não Visitou/Não Realizou Compra (0).

## Agora, vamos separar o que é feature do que é classe.
x = dados[['home','how_it_works','contact']]
y = dados[['bought']]

## Vamos seperar os dados os conjuntos de treino de teste
dados.shape
## Separar 75 para treino e o restante para teste
training_x = x[:75]
training_y = y[:75]
test_x = x[75:]
test_y = y[75:]
print('Treinaremos com %d elementos e testaremos com %d elementos' % (len(training_x),len(test_x)))


## Vamos treinar o nosso modelo
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

model = LinearSVC()
model.fit(training_x, training_y)
previsoes = model.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))

# Estratificando Splits
## A divisão entre elementos de teste e treino feita acima pode ser feita de maneira automatica utilizando uma funcionalidade do sklearn

from sklearn.model_selection import train_test_split
## Neste caso, ele vai retornar 4 itens na seguinte sequencia:
## training_x, test_x, training_y, test_y
## Seus inputs são: x; y; Porcentagem de teste (Entre 0 e 1)

training_x,test_x,training_y,test_y = train_test_split(x,y, test_size = 0.25)
model = LinearSVC()
model.fit(training_x, training_y)
previsoes = model.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))

## Da maneira que rodamos acima, nosso modelo está tomando, de mandeira aleatoria esta divisão entre teste e treino. Isto nos leva à não replicabilidade dos resultados e possíveis resultados tendenciosos devido à essa divisão desproporcional.
## Para resolver isso, utilizamos dois inputs adicionais.

SEED = 20 #Aqui, 'fixamos a aleatoriedade da divisão'
training_x,test_x,training_y,test_y = train_test_split(x,y, random_state = SEED, test_size = 0.25, stratify = y)
## O input 'stratify' faz com que a divisão entre os grupos de modelo e teste siga, na maneira que for possível, a distribuição das Caracteristicas (y)
training_y.value_counts()
test_y.value_counts()
model = LinearSVC()
model.fit(training_x, training_y)
previsoes = model.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))
