# Aula 03 - Classificacao de variáveis categóricas

## Exportando um CSV

import pandas as pd

df = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Machine Learning Classificação por trás dos panos\1. Dados Brutos\Curso Machine Learning_ Introducao a Classificacao - entrada - buscas.csv')
df.head()
raw_x = df[['home','busca','logado']]
raw_y = df['comprou']

### Note que nesste caso, temos uma caracteristica que não é binária, muito menos numérica, a 'busca'. Com isso, podemos utilizar o conceito de 'Variável Dummy' para poder utilizar nossos modelos de classificação
### Para isso, vamos criar novas colunas, cada uma para um possível valor da variável busca, ou seja
### busca_01 (Algoritmo) -> Se buscou algoritmos, 1, caso contrário, 0;
### busca_02 (Java) -> Se buscou Java, 1, caso contrário, 0;
###...
### Com isso, 'trocamos' nossa Feature 'busca' por outras tres que, quando combinadas, são equivalentes à original

## A função .get_dummies do pandas cria, automaticamente colunas de variáveis dummies a partir das colunas já existentes no Dataframe.
x = pd.get_dummies(raw_x)
x.head()

## Em especial, quando a caracteristica não é dummie, ele cria duas colunas. Com isso, pode-se manter os dados originais ou pode-se pegar a segunda coluna criada, uma vez que ela coincide com os dados originais.
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
modelo = MultinomialNB()
modelo.fit(treino_dados,treino_marcacoes)
resultado = modelo.predict(teste_dados)
