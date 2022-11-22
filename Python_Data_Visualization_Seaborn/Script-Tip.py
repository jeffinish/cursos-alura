#Importando as bibliotecas
import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt

pd.set_option("display.max_rows",10) #Seta o máximo de linhas para ser exibida
pd.set_option("display.max_columns",6) #Seta o máximmo de colunas para ser exibida

#Importar a base de dados
data = pd.read_csv("tips.csv")
#print(data.head())

### --- Traduzindo a base --- ###
#print(data.columns)

## -- Traduz as colunas -- ##
renomear = {
    "total_bill":"Valor_da_Conta",
    'tip':"Gorjeta",
    'dessert':"Sobremesa",
    'day':"Dia_da_Semana",
    'time':"Hora_do_dia",
    'size':"Total_de_Pessoas"
}
data = data.rename(columns = renomear)  #Rename aqui renomeia as colunas
#print(data.head())

##  -- Traduzindo os dados -- ##

# - Coluna Sobremsa - #
#print(data.Sobremesa.unique()) #Exibe todos os valores únicos que aparecem na coluna Sobremesa
sim_nao = {
    "No":"Não",
    "Yes":"Sim"
} #Define a relação entre as entradas em portugues e ingles
data.Sobremesa.map(sim_nao) #Aqui, fazemos apenas a associação, mas não alteramos na base de dados
data.Sobremesa = data.Sobremesa.map(sim_nao) #Aqui, fazemos a alteração na base de dados
#print(data.head())

# - Coluna Dia_da_Semana - #
#print(data.Dia_da_Semana.unique())
dia_semana = {
    'Sun':"Domingo",
    'Sat':"Sábado",
    'Thur':"Quinta",
    'Fri':"Sexta"
}
data.Dia_da_Semana = data.Dia_da_Semana.map(dia_semana)
#print(data.head())
#print(data.Dia_da_Semana.unique())

# - Coluna Hora_do_dia - #
#print(data.Hora_do_dia.unique())
hora = {
    "Dinner":"Jantar",
    "Lunch":"Almoço"
}
data.Hora_do_dia = data.Hora_do_dia.map(hora)
#print(data.head())
#print(data.Hora_do_dia.unique())

### --- Análises Estatísticas --- ###

## -- Conferindo a qualidade dos dados -- ##

#print("A base de dados contém {} registros \n".format(data.shape[0]))
#print("Registros não nulos")
#print(data.count())

## -- Valor da Conta x Gorjeta -- ##

valor_gorgeta = sns.scatterplot(x="Valor_da_Conta",y="Gorjeta",data=data)
valor_gorgeta.figure.suptitle("Análises Estatísticas") #Define um suptitulo ao gráfico gerado (Titulo acima do Titulo)
valor_gorgeta.set_title("Valor da Conta x Gorjeta") # Define o titulo (Que na verdade fica abaixo do subtitulo)
valor_gorgeta.set(xlabel = "Valor da Conta",ylabel="Valor da Gorgeta")
valor_gorgeta.figure.savefig("Valor da Conta x Gorjeta.png")
#plt.show()
# - A primeira impressão que temos é que existe uma relação entre o valor da conta e o valor da gorjeta. Quanto maior o valor da conta, maior o valor de gorjeta dado.

# - Criar o campo porcentagem - #

print(data.head(1)) #Print para conferir
data["Porcentagem"] = data["Gorjeta"]/data["Valor_da_Conta"] #Define uma nova coluna a dividindo a coluna Gorjeta pela coluna Valor_da_Conta.
#print(data.head()) #Print para conferir
data.Porcentagem = data.Porcentagem.round(2) #Arredonda a coluna Porcentagem com duas casas decimais
#print(data.head(3))

# - Analisando Valor da Conta x Porcentagem de Gorjeta
porcentagem_conta = sns.scatterplot(x="Valor_da_Conta",y="Porcentagem",data=data)
porcentagem_conta.figure.suptitle("Análises Estatísticas")
porcentagem_conta.set_title("Valor da Conta x Porcentagem de Gorjeta")
porcentagem_conta.set(xlabel = "Valor da Conta", ylabel="Porcentagem de Gorjeta")
porcentagem_conta.figure.savefig("Valor da Conta x Porcentagem de Gorjeta.png")
# - Apesar de termos que o valor da gorjeta aumenta juntamente com o valor da conta, percebemos neste último gráfico que este aumento não é proporcional, isto é, o aumento da gorjeta não é proporcional ao aumento da conta.

# - Criando gráficos de maneira diferente - #
#sns.relplot(x="Valor_da_Conta",y="Porcentagem",kind="line",data=data) #Esse gráfico é meio bosta com o argumento kind=Line.
reg_porcentagem_conta = sns.lmplot(x="Valor_da_Conta", y="Porcentagem", data=data)
reg_porcentagem_conta.figure.suptitle("Análies Estatísticas")
#reg_porcentagem_conta.set_title("Valor da Conta x Gorjeta - Regressão Linear")
reg_porcentagem_conta.set(xlabel = "Valor da Conta",ylabel="Valor da Gorgeta")
reg_porcentagem_conta.figure.savefig("Regressão Linear Valor da Conta x Porcentagem.png")

## -- Pedir sobremesa x Gorjeta -- ##
data.head()
data[data.Sobremesa == "Sim"].describe()
data[data.Sobremesa == "Não"].describe()
sns.catplot(x="Sobremesa",y="Gorjeta",data=data)
sns.relplot(x="Valor_da_Conta",y="Gorjeta",hue="Sobremesa",col="Sobremesa",data=data)
sns.lmplot(x="Valor_da_Conta",y="Gorjeta",col="Sobremesa",hue="Sobremesa",data=data)
sns.lmplot(x="Valor_da_Conta",y="Porcentagem",col="Sobremesa",hue="Sobremesa",data=data)
# - Teste de Hipótese --- #

## H0 - A distribuição da taxa de gorjeta é a mesma nos dois grupos - Com sobremesa x Sem Sobremesa
## H1 - A distribuição da taxa de gorjeta é diferente nos dois grupos
from scipy.stats import ranksums

sobremesa = data.query("Sobremesa == 'Sim'").Porcentagem
sem_sobremesa = data.query("Sobremesa == 'Não'").Porcentagem
r = ranksums(sobremesa,sem_sobremesa)
r
print("O valor do p-value é {}".format(r.pvalue))
### -> Com isso, aceitamos H0.



##### ---- Aula 4 - Comparando e explorando os dias da semana ---- #####

## --- Analisando os dias da semana --- ##

sns.catplot(x="Dia_da_Semana",y="Valor_da_Conta",data=data)
sns.relplot(x="Valor_da_Conta",y="Gorjeta",hue="Dia_da_Semana",col="Dia_da_Semana",data=data)
sns.lmplot(x="Valor_da_Conta",y="Porcentagem",hue="Dia_da_Semana",col="Dia_da_Semana",data=data)
data[data["Dia_da_Semana"] == "Sexta"].describe()
data[data["Dia_da_Semana"] == "Sábado"].describe()
data[data["Dia_da_Semana"] == "Domingo"].describe()
data[data["Dia_da_Semana"] == "Quinta"].describe()
## -> Podemos notar pelos dados, que a Sexta feita é o dia menos movimentado

## - Análise das gorjetas por dia - ##
media_geral_gorjetas = data.Gorjeta.mean()
print("A média do valor de gorjeta é de {}".format(media_geral_gorjetas))

# - Calculando os valores médio das gorjetas em cada dia - #
data.groupby(["Dia_da_Semana"]).mean()[["Valor_da_Conta","Gorjeta","Porcentagem"]]  # - Aqui, calculamos a média dos valores Agrupados por dia da semana - O argumento [[]] indica quais colunas queremos que sejam exibidas.

## - Teste de hipótese - #
# H0 - A distribuição do valor da conta é igual para o Sábado e no Domingo
# H1 - A distribuição do valor da conta é diferente para o Sábado e no Domingo

Conta_Domingo = data.query("Dia_da_Semana == 'Domingo'").Valor_da_Conta
Conta_Sabado = data.query("Dia_da_Semana == 'Sábado'").Valor_da_Conta
r_conta = ranksums(Conta_Domingo,Conta_Sabado)
print("O valor do p-value é {}".format(r_conta.pvalue))
# -> Com isso, mantetemos a H0 -> A distribuição no valor da conta no sábado e no domingo são estatísticamente iguais. (Com 95% de confiança.)


#### ---- Aula 5 - Distribuição de frequência e teste de hipótese ---- ####

## - Análise do horário do dia -- ##

# - Gerando alguns gráficos - #
sns.catplot(x="Hora_do_dia",y="Valor_da_Conta",kind="swarm",data=data)
sns.violinplot(x="Hora_do_dia",y="Valor_da_Conta",data=data)
sns.boxplot(x="Hora_do_dia",y="Valor_da_Conta",data=data)
# - Gerando histogramas - #
# Para gerar histogramas, precisamos trabalhar com Querys, por isso as definições abaixo
almoco = data.query("Hora_do_dia == 'Almoço'").Valor_da_Conta
jantar = data.query("Hora_do_dia == 'Jantar'").Valor_da_Conta
sns.displot(almoco)
sns.displot(jantar)

## - Teste de Hipotese - ##

data.groupby(["Hora_do_dia"]).mean()[["Valor_da_Conta","Gorjeta","Porcentagem"]]
#H0 - A distribuição dos valores do almoço e do jantar são iguais
#H1 - A distribuição dos valores do almoço e do jantar são diferentes
r_refeicao = ranksums(jantar,almoco)
print("O valor do p-value é {}".format(r_refeicao.pvalue))

# Aceitamos a Hipotese alternativa com 99% de probablidade.
