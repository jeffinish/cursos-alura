# Importando bibliotecas

import pandas as pd

# Importando a base de Dados

dados = pd.read_csv(r'G:\My Drive\1. ESTUDO\Alura - Python Pandas Tratando e analisando dados\Dados Tratados\aluguel_residencial_m2.csv',sep=';')

## Capitulo 1 - Criando Agrupamentos

grupo_bairro = dados.groupby('Bairro')
grupo_bairro
### Uma variável do tipo groupby é uma lista de DataFrame consolidada pelos valors da variável que escolhemos
### 'Guardando' os indices onde cada valor aparece
grupo_bairro.groups

for bairro, data in grupo_bairro:
    ### Aqui, são DataFrames para cada bairro
    print(data)


### Feito isso, podemos calcular a média do valor do aluguel para cada bairro, por exemplo
for bairro, dados in grupo_bairro:
    print('{} -> {}'.format(bairro,dados.Valor.mean()))


### Porém, felizmente a criação de Groupby nos fornece maneiras de calcular a média, por exemplo, de uma maneira muito mais simples.

grupo_bairro.Valor.mean()
grupo_bairro[['Valor','Condominio']].mean().round(2)

### Capítulo 04 - Estatisticas descritivas
grupo_bairro['Valor'].describe().round(2)

### O método 'aggregate' nos permite escolhe quais das medidas queremos
### Além disso, podemos renomear as colunas utilizando o método 'rename'
grupo_bairro['Valor'].aggregate(['min','max',]).rename(columns = {'min':'Mínimo','max':'Máximo'})

### Vamos criar alguns gráficos agora :)
    %matplotlib inline
    import matplotlib.pyplot as plt
    plt.rc('figure',figsize=(20,10))

fig_std = grupo_bairro['Valor'].std().plot.bar(color = 'blue')
fig_std.set_ylabel('Valor do Aluguel')
fig_std.set_title('Desvio Padrão do aluguel por Bairro',{'fontsize':22})
fig_mean = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig_mean.set_ylabel('Valor do Aluguel')
fig_mean.set_title('Valor médio do aluguel por Bairro',{'fontsize':22})

## Captulo 06 - (Extra) Criando Faixas de Valor.

dados_extra = dados.copy()
### Vamos criar, a partir da coluna 'Quartos', um campo com faixas de quantidades de quartos: 1 e 2 Quartos; 3 e 4 Quartos; 5 e 6 Quartos, 7 quartos ou mais.
### Criamos uma lista com os limites inferior e superior do nosso interesse assim como os limites de cada uma das classes.
classes = [0,2,4,6,100]
quartos = pd.cut(dados.Quartos,classes)
quartos
pd.value_counts(quartos)

### Agora, podemos fazer ajustes para nosso dado ficar mais bem apresentado
labels = [' 1 e 2 Quartos', '3 e 4 Quartos','5 e 6 Quartos','7 quartos ou mais.']
quartos = pd.cut(dados.Quartos,classes,labels = labels)
quartos
pd.value_counts(quartos)
### Existe um argumento que inclui o limite inferior também
quartos = pd.cut(dados.Quartos,classes,labels = labels,include_lowest=True)
quartos
pd.value_counts(quartos)
