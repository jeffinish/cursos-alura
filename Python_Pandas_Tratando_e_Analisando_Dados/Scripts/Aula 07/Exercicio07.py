# Exercicio 07 - Testando Moedas

import pandas as pd

### Importando as moedas
m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'
### C = Cara; c = Coroa

### Precisamos da função list para separar os lançamentos
eventos = {'m1': list(m1),
            'm2': list(m2),
            'm3': list(m3),
            'm4': list(m4),
            'm5': list(m5)}

eventos

### Criando o DataFrame com os eventos
moedas = pd.DataFrame(eventos)
moedas

df = pd.DataFrame(data = ['Cara','Coroa'], index=['c','C'],columns = ['Faces'])
df

### Agora, base concatenar as colunas para cada moeda com os valores do value_counts
for item in moedas:
    df = pd.concat([df, moedas[item].value_counts()],axis=1)

df
