# Aula 02 - Importando, Classificando e validando um modelo

import pandas as pd

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Machine Learning Classificação por trás dos panos\1. Dados Brutos\acesso.csv')
dados.head()

x = dados[['acessou_home','acessou_como_funciona','acessou_contato']]
y = dados['comprou']

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(x,y)


usuario_teste = [1,0,1]
print(modelo.predict([usuario_teste]))

## Treinando e testando o algoritmo com metade dos dados
