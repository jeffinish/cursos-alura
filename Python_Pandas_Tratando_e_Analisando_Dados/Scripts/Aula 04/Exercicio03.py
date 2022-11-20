# Importanto bibliotecas

import pandas as pd

numeros = [i for i in range(11)]
numeros
letras = [chr(i + 65) for i in range(11)]
letras
nome_coluna = ['N']
nome_coluna
df = pd.DataFrame(data = numeros, index = letras, columns = nome_coluna)
df

## i%2 é o resto da divisão (mod 2)
selecao = df['N'].isin([i for i in range(11) if i % 2 == 0])
selecao
df = df[selecao]
df
