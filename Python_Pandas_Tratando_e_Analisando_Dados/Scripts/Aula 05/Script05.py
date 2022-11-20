# Importando bibliotecas

import pandas as pd

# Importando a base de Dados

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial.csv',sep=';')

## Capítulo 02 - Seleções e frequências

### Agora, queremos realizar certas análises baseadas na base de dados que geramos anteriormente. Estas são:

# Selecione somente os imóveis classificados com tipo 'Apartamento'

selecao_1 = dados.Tipo == 'Apartamento'
selecao_1
n1 = dados[selecao_1]
n1.shape[0]
# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
selecao_2 = (dados.Tipo == 'Casa') | (dados.Tipo == 'Casa de Condomínio') | (dados.Tipo == 'Casa de Vila')
selecao_2
n2 = dados[selecao_2]
n2.shape[0]
# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
selecao_3 = (dados.Area >= 60) &  (dados.Area <= 100)
selecao_3
n3 = dados[selecao_3]
n3.shape[0]
# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao_4 = (dados.Quartos >=4) & (dados.Valor < 2000)
selecao_4
n4 = dados[selecao_4]
n4.shape[0]


print('Numero de imóveis classificados com tipo Apartamento: {}'.format(n1.shape[0]))
print('Numero de imóveis classificados com tipos Casa, Casa de Condomínio e Casa de Vila: {}'.format(n2.shape[0]))
print('Numero de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites: {}'.format(n3.shape[0]))

print('Numero de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00: {}'.format(n4.shape[0]))
