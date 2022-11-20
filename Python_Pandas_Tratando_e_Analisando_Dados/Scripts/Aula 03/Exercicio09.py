import pandas as pd

## Letra A) -> Errada

df1 = pd.DataFrame({'A': {'X': 1}, 'B': {'X': 2}})
df1
df2 = pd.DataFrame({'C': {'X': 3}, 'D': {'X': 4}})
df2
pd.concat([df1, df2])


## Letra B) -> Errada

## Letra C)
dados = [[1, 2, 3], [4, 5, 6]]
dados
index = 'X,Y'.split(',')
index
columns = list('CBA')[::-1]
columns
df = pd.DataFrame(dados, index, columns)
df
