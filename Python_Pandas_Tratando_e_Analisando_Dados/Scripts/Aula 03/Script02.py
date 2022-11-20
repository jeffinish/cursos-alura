# Importando bibliotecas

import pandas as pd

# Importando a base de Dados

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Brutos\aluguel.csv',sep=';')
dados.head()

### Vamos focar nos Tipos de imóveis. Para isso, vamos criar um variável.

tipo_de_imovel = dados.Tipo
tipo_de_imovel

### Note que nossa nova variável é bem semelhante ao dataframe que tinhamos anteriormente, porém, se utilizamos o type(), notamos que na verdade temos uma 'Series', ou seja, uma lista de valores, cada um com seus respectivos índices.
type(tipo_de_imovel)
### Desta forma, podemos dizer que um DataFrame é uma coleção de Series

### Para buscar os valores unicos na nossa Series, temos o metodo .drop_duplicates()
tipo_de_imovel.drop_duplicates()
### Acima, criamos apenas uma visualização e não associamos à nenhuma variável e também não alteramos a nossa variável original
tipo_de_imovel
### Felizmente, alguns métodos do pandas admitem o argumento 'inplace = ', que fazem com que a variável em questão seja alterada após execução do comando, sem a necessidade de criarmos uma nova variável para fazer esta alteração
tipo_de_imovel.drop_duplicates(inplace=True)
tipo_de_imovel


## Seção 04 - Redefinindo o Index

### Continuando o que fizemos acima, vamos criar um DataFrame a partir da series que criamos no passo anterior. Além de criar o DataFrame, vamos reiniciar os índices
tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
tipo_de_imovel.reset_index(drop=True)
tipo_de_imovel.columns.name = 'id'
tipo_de_imovel
