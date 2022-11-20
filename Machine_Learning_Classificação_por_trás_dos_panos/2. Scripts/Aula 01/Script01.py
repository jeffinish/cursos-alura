# Aula 01 - Classificando emails, animais e muito mais

## Classificação entre 0 e 1

### Vamos classificar dois tipos de animais. Porcos (1) e Cachorros (-1)
### Nossas caracteristicas são:
### É gordinho? Sim (1), Não (0)
### Tem Perna Curta? Sim (1), Não (0)
### Faz 'au au'? Sim (1), Não (0)

porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [0,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]

marcacoes = [1,1,1,-1,-1,-1]


### Este elemento é um Cachorro ou é um porco?
misterioso1 = [1,1,1]


from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados,marcacoes)
modelo.predict([misterioso1])
print(modelo.predict([misterioso1]))
### Ou seja, este modelo acredita que o animal misterioso é um Cachorro (-1).

misterioso2 = [1,0,0]
modelo.predict([misterioso2])
print(modelo.predict([misterioso2]))

### Podemos testar vários elementos de uma vez
misterioso = [misterioso1,misterioso2]
modelo.predict(misterioso)
print(modelo.predict(misterioso))

## Sabendo a taxa de acerto

### Vamos testar nosso modelo com animais que sabemos a resposta
misterioso1 = [1,1,1] #É um cachorro
misterioso2 = [1,0,0] #É um porco
misterioso3 = [0,0,1] #É um cachorro
teste = [misterioso1,misterioso2,misterioso3]
marcacoes_teste = [-1,1,-1]

modelo.predict(teste)

## Exemplo no mundo web
### Vamos cliassificar agora usuários baseado nas páginas que ele acessou na webpage.
### Feature: Home, Como Funciona, Contato -> Sim (1), Não (0)
### Classificação: Comprou -> Sim (1), Não (0)

1,0,1,1
0,1,0,0
1,1,0,1
0,1,0,1
