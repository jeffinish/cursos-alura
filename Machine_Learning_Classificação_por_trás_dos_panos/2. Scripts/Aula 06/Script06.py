# Testando diferentes modelos e validando

## Registrando os testes

### Aqui, vamos chamar atenção sobre a importância de saber avaliar quais teste fazer.
### Vamos comparar o resultado do algortimo variando as features utilizadas



import pandas as pd

df = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Machine Learning Classificação por trás dos panos\1. Dados Brutos\Curso Machine Learning_ Introducao a Classificacao - entrada - buscas2.csv')
df.head()

## Utilizando todas as features

raw_x = df[['home','busca','logado']]
raw_y = df['comprou']

x = pd.get_dummies(raw_x)
x.head()

y = pd.get_dummies(raw_y)[1]
y.head()

## Treinando e testando o algoritmo
porcentagem_de_treino = 0.9
tamanho_de_treino = porcentagem_de_treino*len(y)
treino_dados = x[:int(tamanho_de_treino)]
treino_marcacoes = y[:int(tamanho_de_treino)]
tamanho_de_teste = len(y)-tamanho_de_treino
teste_dados = x[-int(tamanho_de_teste):]
teste_marcacoes = y[-int(tamanho_de_teste):]
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)
resultado = modelo.predict(teste_dados)
acuracia = accuracy_score(teste_marcacoes,resultado)
print("A acurácia do algoritmo (Com todas as features) foi de %.2f%%" % (acuracia*100))


## Utilizando apenas 'Home' e 'Busca'
raw_x = df[['home','busca']]
raw_y = df['comprou']
x = pd.get_dummies(raw_x)
x.head()
y = pd.get_dummies(raw_y)[1]
y.head()
## Treinando e testando o algoritmo
porcentagem_de_treino = 0.9
tamanho_de_treino = porcentagem_de_treino*len(y)
treino_dados = x[:int(tamanho_de_treino)]
treino_marcacoes = y[:int(tamanho_de_treino)]
tamanho_de_teste = len(y)-tamanho_de_treino
teste_dados = x[-int(tamanho_de_teste):]
teste_marcacoes = y[-int(tamanho_de_teste):]
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)
resultado = modelo.predict(teste_dados)
acuracia = accuracy_score(teste_marcacoes,resultado)
print("A acurácia do algoritmo (Com todas as features) foi de %.2f%%" % (acuracia*100))

## Utilizando apenas 'Home' e 'Logado'
raw_x = df[['home','logado']]
raw_y = df['comprou']
x = pd.get_dummies(raw_x)
x.head()
y = pd.get_dummies(raw_y)[1]
y.head()
## Treinando e testando o algoritmo
porcentagem_de_treino = 0.9
tamanho_de_treino = porcentagem_de_treino*len(y)
treino_dados = x[:int(tamanho_de_treino)]
treino_marcacoes = y[:int(tamanho_de_treino)]
tamanho_de_teste = len(y)-tamanho_de_treino
teste_dados = x[-int(tamanho_de_teste):]
teste_marcacoes = y[-int(tamanho_de_teste):]
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)
resultado = modelo.predict(teste_dados)
acuracia = accuracy_score(teste_marcacoes,resultado)
print("A acurácia do algoritmo (Com todas as features) foi de %.2f%%" % (acuracia*100))


# Utilizando apenas 'Busca' e 'Logado'

raw_x = df[['busca','logado']]
raw_y = df['comprou']

x = pd.get_dummies(raw_x)
x.head()

y = pd.get_dummies(raw_y)[1]
y.head()

## Treinando e testando o algoritmo
porcentagem_de_treino = 0.9
tamanho_de_treino = porcentagem_de_treino*len(y)
treino_dados = x[:int(tamanho_de_treino)]
treino_marcacoes = y[:int(tamanho_de_treino)]
tamanho_de_teste = len(y)-tamanho_de_treino
teste_dados = x[-int(tamanho_de_teste):]
teste_marcacoes = y[-int(tamanho_de_teste):]
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)
resultado = modelo.predict(teste_dados)
acuracia = accuracy_score(teste_marcacoes,resultado)
print("A acurácia do algoritmo (Com todas as features) foi de %.2f%%" % (acuracia*100))

# Utilizando apenas 'Busca'

raw_x = df[['busca']]
raw_y = df['comprou']

x = pd.get_dummies(raw_x)
x.head()

y = pd.get_dummies(raw_y)[1]
y.head()

## Treinando e testando o algoritmo
porcentagem_de_treino = 0.9
tamanho_de_treino = porcentagem_de_treino*len(y)
treino_dados = x[:int(tamanho_de_treino)]
treino_marcacoes = y[:int(tamanho_de_treino)]
tamanho_de_teste = len(y)-tamanho_de_treino
teste_dados = x[-int(tamanho_de_teste):]
teste_marcacoes = y[-int(tamanho_de_teste):]
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)
resultado = modelo.predict(teste_dados)
acuracia = accuracy_score(teste_marcacoes,resultado)
print("A acurácia do algoritmo (Com todas as features) foi de %.2f%%" % (acuracia*100))
