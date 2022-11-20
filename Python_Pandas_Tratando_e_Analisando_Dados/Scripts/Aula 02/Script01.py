# Importando a bibliotca
import pandas as pd

# Importando a base de dados
pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Brutos\aluguel.csv')
## Note que ao importar o nosso arquivo csv, o separador default é ',', porém nosso arquivo utiliza ';'. Para resolver este problema, vamos incluir o argumento 'sep=;' na nossa importação

pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Brutos\aluguel.csv',sep=';')

## O que foi feito acima, foi apenas uma visualização da nossa base de dados, ela não foi 'guardada' em nenhum lugar. Para isso, podemos associar este comando à uma varíavel.

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Brutos\aluguel.csv',sep=';')
dados

### O objeto criado acima é um DataFrame
type(dados)

### E para obtemos mais informações sobre este objeto, podemos utilizar o seguinte comando:
dados.info()

### Um método interessante que os DataFrame possui é o .head(n) (Default n=5), que nos fornece as n primeiras linhas deste objeto
dados.head()


### O metodo .dtypes nos apresenta o tipo de cada coluna
dados.dtypes

### Uma maneira mais elegante de apresentar os dados acima é criar um DataFrame com eles. Para isso, fazemos:
pd.DataFrame(dados.dtypes,columns=['Tipos de Dados'])
### Porém, note que a coluna de variáveis está sem título. Para resolver este problema, podemos fazer o seguinte:
tipos_de_dados = pd.DataFrame(dados.dtypes,columns=['Tipos de Dados'])
tipos_de_dados.columns.name = 'Variáveis'
tipos_de_dados

### Outra informação interessante com relação à base de dados, são suas dimensões: quantidade de registros e de variáveis. Isto é obtido através do método .shape

dados.shape
dados.shape[0]
dados.shape[1]
print(f'A base de dados possui {dados.shape[0]} entradas')
print('A base de dados possui {} variáveis'.format(dados.shape[1]))
