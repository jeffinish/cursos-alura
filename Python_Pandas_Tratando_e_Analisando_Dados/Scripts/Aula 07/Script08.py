# Importando bibliotecas

import pandas as pd

# Importando a base de Dados

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial_novo.csv',sep=';')

## Capitulo 02 - Criando novas variáveis

### Vamos criar novas variáveis a partir das que já temos:

dados.head()

### Criando variável com Valor Bruto do Aluguel
dados['Valor Bruto'] = dados.Valor + dados.Condominio + dados.IPTU
dados.head()

### Criando variável com Valor por m2
dados['Valor por m2'] = round(dados.Valor / dados.Area,2)
dados.head()

### Criando variável com Valor Bruto por m2
dados['Valor bruto por m2'] = round(dados['Valor Bruto']/dados['Area'],2)
dados.head()

### Vamos agrupar todos os valores que representam casa em uma única variável
casa = ['Casa', 'Casa Condomínio','Casa de Vila']
### Vamos utilizar uma função que associa 'Casa' aos valores da coluna 'Tipo' que estão contidos na lista definida acima e 'Apartamento' caso contrário.
dados['Tipo Agregado'] = dados.Tipo.apply(lambda x: 'Casa' if x in casa else 'Apartamento')
dados


## Capítulo 04 - Excluindo variáveis

### Vamos excluir as variáveis que estão relacionadas com IPTU, uma vez que este possui valores ausentes.

### Uma maneira é utilizar a função del
del dados['Valor Bruto']
dados.head()

### Outra maneira é utilizar o método pop
dados.pop("Valor bruto por m2")
dados.head()

### Outra é o drop
dados.drop('IPTU',axis=1,inplace=True)
dados.head()

dados.to_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial_m2.csv',sep=';',index=False)
