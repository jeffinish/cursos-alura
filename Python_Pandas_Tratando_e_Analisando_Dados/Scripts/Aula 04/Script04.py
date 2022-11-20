# Importanto bibliotecas

import pandas as pd

# Importando a base de Dados

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Brutos\aluguel.csv',sep=';')
dados.head()

## Capítulo 2 - Imóveis residenciais

### Nosso objetivo agora é focar apenas em imóveis residenciais. Para isso, vamos extrair novamente a lista de todos os tipos de imóveis.

list(dados.Tipo.drop_duplicates())

### Da lista acima, vamos selecionar apenas os residenciais e associá-los à uma variável

residencial = ['Quitinete',
 'Casa',
 'Apartamento',
 'Casa de Condomínio',
 'Casa de Vila']
residencial

### Vamos utilizar a lista acima para filtrar nosso dataframe original. Para isso, vamos usar o metodo .isin()

dados.Tipo.isin(residencial)
### A partir da series acima, podemos criar uma variável booleana (True or False), a partir do nosso DataFrame original onde, se a coluna 'Tipo' é um dos elementos da lista, o elemento é marcado como 'True' e caso contrário, como 'False'
selecao = dados.Tipo.isin(residencial)

### Com a lista booleana abaixo, podemos filtrar nosso DataFrame de maneira simples, utilizando a lista como argumento.
dados_residencial = dados[selecao]
dados_residencial
### Podemos verificar se o filtro foi aplicado
dados_residencial.Tipo.drop_duplicates()

dados_residencial.reset_index(drop=True)

## Capitulo 4 - Exportando base de dados

### Vamos exportar o DataFrame com os imoveis residenciais para um arquivo csv para utilizarmos no futuro
dados_residencial.to_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial.csv', sep=';',index=False)
pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial.csv',sep=';')
