# Importando bibliotecas

import pandas as pd

# Importando a base de Dados

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial.csv',sep=';')

## Capítulo 02 - Tratando valores nulos

dados.notnull() ## Apresenta os valores que não são nulo como 'True'
dados.isnull() ## Apresenta os valores são nulos como 'True'

dados.info()

### Vamos ver quais os apartamentos que possuem 'Valor' como nulo
dados[dados['Valor'].isnull()]

### Vamos remover estes registros do nosso DataFrame
dados.dropna(subset=['Valor'],inplace=True)
dados.shape[0]
dados[dados['Valor'].isnull()]


## Capitulo 04 - Tratamento Condicional

### Vamos analisar agora a coluna 'Condominio'
dados[dados['Condominio'].isnull()].shape[0]
selecao = (dados.Tipo == 'Apartamento') & (dados['Condominio'].isnull())
selecao
### Porém, note que a seleção acima é exatamente o oposto do que nós queremos remover, para isso, podemos inverter o valor de uma variável booleana utilizando '~'
dados = dados[~selecao]
dados.shape[0]

### Agora, para tratar os outros valores nulos, temos duas opçoes:
dados.fillna(0) #-> Substitui todos os valores nulos por 0, independente da nome_coluna
dados.fillna({'Condominio':0,'IPTU':0}) #-> Atribui a cada coluna, um valor para substituir os valores nulos

dados = dados.fillna({'Condominio':0,'IPTU':0})
dados.info()

dados.to_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial_novo.csv',sep=';',index=False)
