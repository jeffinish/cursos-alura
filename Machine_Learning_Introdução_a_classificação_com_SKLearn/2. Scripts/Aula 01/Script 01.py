# Aula 01
# O primeiro projeto

## Classificação entre Cachorros e Porcos
## Features - Caracteristicas - Eixo X
## - Têm pelo longo?
## - Tem perna curta?
## - Faz "Au Au"

## Classificação - É cachorro (0) ou porco (1) - Eixo Y

## A estimação desta classificação não é exata. Podemos medir a acurácia do nosso modelo

# Primeiro treino e teste de um modelo

## Vamos criar nossos "animais"
## Features - Caracteristicas - Sim (1) Não (0)
## - Têm pelo longo?
## - Tem perna curta?
## - Faz "Au Au"

porco1 = [0,1,0] # Não tem pelo longo; Tem perna curta; Não faz Au Au;
porco2 = [0,1,1]
porco3 = [1,1,0]

cachorro1 = [0,1,1]
cachorro2 = [1,0,1]
cachorro3 = [1,1,1]

dados = [porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]

## Classificação : Porco (1); Cachorro (0)
## Associamos aos nossos animais conhecidos, suas devidas classificações
classes = [1,1,1,0,0,0]

## Vamos utilizar o pacote sklearn para criar nosso modelo de estimação
from sklearn.svm import LinearSVC

model = LinearSVC()
## Para utilizar o modelo, utilizamos a função fit, cujos inputs são: X -> Features, Y-> Classificação conhecida
model.fit(dados,classes)
## Uma vez tendo o modelo adaptado aos nossos dados, podemos utilizá-lo pra prever a classificação de animais desconhecidos

animal_misterioso = [1,1,1] # Tem pelo longo; Tem perna curta; Faz Au Au -> Esperamos um cachorro?
## OBS: o .predict espera uma lista de valores, por isso colocamos [animal_misterioso]
model.predict([animal_misterioso])
print(model.predict([animal_misterioso]))
## Ou seja, o nosso modelo acredita que o nosso animal, com essas features, é um cachorro.

## Vamos rodar agora para vários animais, a principio, desconhecidos
misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,0,1]
teste = [misterio1,misterio2,misterio3]
model.predict(teste)

## Caso já soubessemos a classificação dos animais utilizados para teste, podemos avaliar o desempenho do nosso modelo
testes = [misterio1,misterio2,misterio3]
previsoes = model.predict(testes)
print(previsoes) #Ou seja, o modelo acredita que os animais são, respectivamente: Cachorro; Porco; Cachorro
testes_classes = [0,1,1] # Ou seja, os animais misteriosos eram, na verdade: Cachorro; Porco; Porco

## Vamos agora, avaliar a acurácia do nosso modelo comparando as duas arrays
corretos = (previsoes == testes_classes).sum() # Número de verdadeiros
print(corretos) ## Ou seja, o modelo acertou 2.
total = len(testes)
taxa_de_acerto = corretos/total
print("A Taxa de Acerto é de: ",taxa_de_acerto*100)


## Este cálculo feito acima pode ser feito utilizado uma feature da biblioteca sklearn chamada accuracy_score
from sklearn.metrics import accuracy_score

taxa_de_acerto = accuracy_score(testes_classes,previsoes)
print(taxa_de_acerto)


# Padronização dos nome
## Apesar de termos nosso modelo funcionando corretamente, podemos melhorar a maneira de chamar os nossos dados para ficar mais claro. Vamos utilizar
## training_x para features e training_y para classes (labels) de treino
training_x = [porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]
training_y = [1,1,1,0,0,0]
model.fit(training_x,training_y)

## test_x e test_y para features e classes de teste
test_x = [misterio1,misterio2,misterio3]
test_y = [0,1,1]
previsoes = model.predict(test_x)
previsoes
taxa_de_acerto = accuracy_score(test_y,previsoes)
print("A Taxa de Acerto é de: %.2f" % (taxa_de_acerto*100))
