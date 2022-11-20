# Importando bibliotecas

import pandas as pd



## Capítulo 06 - Criando uma Series

data = [1,2,3,4,5]
s = pd.Series(data)
s

### Podemos criar índices especiais para nossa series, basta apenas definir os indices anteriormente

index = ['Linha' + str(i) for i in range(5)]
index

s = pd.Series(data,index=index)
s

### Outra maneira de alterar o indice é através de um dicionário. Desta forma, podemos criar a Series diretamente, sem precisar alterar o index

data = {'Linha' + str(i):i+1 for i in range(5)}
data

s1 = pd.Series(data)
s1


### Uma vantagem de se trabalhar com series é a facilidade em realizar operações matemáticas e relacionar várias series com mesmo.

s1+s


## Capítulo 07 - Concatenando dataframes

data = [[1,2,3],[4,5,6],[7,8,9]]
data

df1 = pd.DataFrame(data)
df1

### Criando rotulo para colinhas
index = ['Linha' + str(i) for i in range(3)]
df1 = pd.DataFrame(data,index=index)
df1

### Criando rotulo para colunas
columns = ['Columns' + str(i) for i in range(3)]
df1 = pd.DataFrame(data,index=index,columns=columns)
df1

### Outra maneira de criar um Dataframe é através de dicionários
data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}
data

df2 = pd.DataFrame(data,index=index,columns=columns)
df2
df3 = pd.DataFrame(data,index=index,columns=columns)

### Concatenar Dafaframe

df1[df1 > 0] = 'A'
df1
df2[df2 > 0] = 'B'
df2
df3[df3 > 0] = 'C'
df3

df4 = pd.concat([df1,df2,df3])
df4

df5 = pd.concat([df1,df2,df3],axis=1)
df5
