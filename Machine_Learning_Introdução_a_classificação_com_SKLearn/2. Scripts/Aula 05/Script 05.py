# Aula 05

## Trabalhando num novo projeto

import pandas as pd
import numpy as np
uri = 'https://gist.githubusercontent.com/guilhermesilveira/4d1d4a16ccbf6ea4e0a64a38a24ec884/raw/afd05cb0c796d18f3f5a6537053ded308ba94bf7/car-prices.csv'
raw_data = pd.read_csv(uri)
raw_data.head()
## Features:
## mileage_per_year -> Milhas por ano
## model_year -> Ano do modelo
## price -> Valor do anuncio

## Classe : sold -> yes,no
trocar = {'yes':1,'no':0}
raw_data.sold = raw_data.sold.map(trocar)
raw_data.head()

## Preparando os dados
### Vamos criar uma nova coluna com a idade do modelo, uma vez que vamos ter dados 'mais bonitos' para trabalhar no modelo
from datetime import datetime
ano_atual = datetime.today().year
raw_data['age'] = ano_atual - raw_data.model_year
raw_data.head()
raw_data = raw_data.drop(columns=['Unnamed: 0','model_year'],axis=1)
raw_data.head()

### Separando os dados

x = raw_data[['mileage_per_year','price','age']]
x.head()
y = raw_data['sold']
y.head()


## Como vimos nas outras atividades, é sempre termos um teste básico para avaliarmos nosso modelo. Como isso é algo que sempre acontece, o proprio sklearn possui uma biblioteca para fazer isso
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

SEED = 20
np.random.seed(SEED)
training_x,test_x,training_y,test_y = train_test_split(x,y, random_state = SEED, test_size = 0.25, stratify = y)

## Como default, o DummyClassifier de acordo com a classe que mais aparece

from sklearn.dummy import DummyClassifier
dummy_most_frequent = DummyClassifier(strategy='most_frequent')
dummy_most_frequent.fit(training_x,training_y)
previsoes = dummy_most_frequent.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia do Dummy (most_frequent) foi de %.2f%%" % (acuracia*100))

## Vamos agora, utilizar outra estratégia para a variavel dummy
from sklearn.dummy import DummyClassifier
dummy_stratified = DummyClassifier(strategy='stratified')
dummy_stratified.fit(training_x,training_y)

previsoes = dummy_stratified.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia do Dummy (Stratified) foi de %.2f%%" % (acuracia*100))


## Agora, vamos fazer os ajustes finais para podermos utilizar o SVC

from sklearn.preprocessing import StandardScaler

SEED = 20
np.random.seed(SEED)
raw_training_x,raw_test_x,training_y,test_y = train_test_split(x,y, random_state = SEED, test_size = 0.25, stratify = y)
print('Treinaremos com %d elementos e testaremos com %d elementos' % (len(raw_training_x),len(raw_test_x)))

scaler = StandardScaler()
scaler.fit(raw_training_x) # Baseado nas features, o modelo vai aprender como normalizar os dados
## Normalizamos as features baseados na nova medida
training_x = scaler.transform(raw_training_x)
test_x = scaler.transform(raw_test_x)

model = SVC()
model.fit(training_x, training_y)
previsoes = model.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))


## Arvore de Decis'ao e Visualizando as decisoes de um estimador

## Apesar da qualidade da classificação obtida, esse tipo de algoritmo não nos permite ver quais foram as razões por tras das escolhas feitas.
## Porém existem outros tipos que permitem e é o que veremos agora.

from sklearn.tree import DecisionTreeClassifier ## Importa o algoritmo de arvore de decisão
from sklearn.tree import export_graphviz ## Importa a biblioteca para exportar a arvore de decisao
import graphviz ## Importa a biblioteca que plota o grafico de decisão

SEED = 20
np.random.seed(SEED)
raw_training_x,raw_test_x,training_y,test_y = train_test_split(x,y, random_state = SEED, test_size = 0.25, stratify = y)
print('Treinaremos com %d elementos e testaremos com %d elementos' % (len(raw_training_x),len(raw_test_x)))

scaler = StandardScaler()
scaler.fit(raw_training_x) # Baseado nas features, o modelo vai aprender como normalizar os dados
## Normalizamos as features baseados na nova medida
training_x = scaler.transform(raw_training_x)
test_x = scaler.transform(raw_test_x)


model = DecisionTreeClassifier(max_depth=2)
## Max depth indica quantos níveis nossa arvore vai ter.
model.fit(training_x, training_y)
previsoes = model.predict(test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))

features = x.columns
dot_data = export_graphviz(model,out_file=None,
                            feature_names = features,
                            filled=True,
                            rounded=True,
                            class_names = ['nao','sim'])
## features_names indica qual o nome das feaatures que vão aparecer
grafico = graphviz.Source(dot_data)
grafico

## Note que, aqui os preços passaram por uma normalização, o que faz com que a feature 'price' fique com valores estranhos.
## Porém, uma vantagem das arvores de decisão é que elas funcionam bem mesmo com os dados não normalizados.
## Vamos rodar o mesmo código, agora sem normalizar

SEED = 20
np.random.seed(SEED)
raw_training_x,raw_test_x,training_y,test_y = train_test_split(x,y, random_state = SEED, test_size = 0.25, stratify = y)
print('Treinaremos com %d elementos e testaremos com %d elementos' % (len(raw_training_x),len(raw_test_x)))


model = DecisionTreeClassifier(max_depth=2)
## Max depth indica quantos níveis nossa arvore vai ter.
model.fit(raw_training_x, training_y)
previsoes = model.predict(raw_test_x)
acuracia = accuracy_score(test_y,previsoes)
print("A acurácia foi de %.2f%%" % (acuracia*100))

features = x.columns
dot_data = export_graphviz(model,out_file=None,
                            feature_names = features,
                            filled=True,
                            rounded=True,
                            class_names = ['nao','sim'])
## features_names indica qual o nome das feaatures que vão aparecer
grafico = graphviz.Source(dot_data)
grafico
