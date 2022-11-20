# Aula 01 - Capítulo 02 : Validando um CPF

### Para a validação de um CPF, vamos primeiramente conferir se ele possui 11 caracteres.

cpf = '10044387610' #Aqui, precisamos ter o CPF como string, uma vez que elementos inteiros não admitem método 'len'
tamanho_cpf = len(cpf)
print(tamanho_cpf)

### Porém, note que da maneira que foi feita acima, o usuário precisaria digitar o cpf entre aspas, o que pode ser um problema. Para resolver isso, podemos sobescrever a variváel

cpf = 10044387610
cpf = str(cpf) #Transforma o inteiro em string
tamanho_cpf = len(cpf)
print(tamanho_cpf)


## Vamos validar nosso arquivo CPF.py

from CPF import CPF

cpf1 = 10044387610
cpf2 = 12345

objeto_cpf = CPF(cpf1) ### Rodou sem erros

objeto_cpf = CPF(cpf2) ### Deu um erro!

### Para exibir o cpf formatado do jeito que a gente, vamos 'fatiar' o input da seguinte maneira
cpf = '10044387610' # Lembrando de sempre usar string
fatia_um = cpf[:3]
fatia_um
fatia_dois = cpf[3:6]
fatia_dois
fatia_tres = cpf[6:9]
fatia_tres
fatia_quatro = cpf[9:]
fatia_quatro
cpf_formatado = "{}.{}.{}-{}".format(fatia_um,
                                    fatia_dois,
                                    fatia_tres,
                                    fatia_quatro)
cpf_formatado


## Vamos validar agora a utilização da máscara que criamos
cpf1 = 10044387610
cpf2 = 12345

objeto_cpf = CPF(cpf1) ### Rodou sem erros
print(objeto_cpf)

objeto_cpf = CPF(cpf2) ### Deu um erro!

## Capítulo 03 - Pacotes Python
### Além da validação da quantidade de caracteres que o CPF possui, existem outras validaçoes para saber se, mesmo com a quantidade de caracteres correta o cpf em questão é um cpf válido.
### Para isso, vamos instalar a biblioteca validade-docbr e utilizá-la no nosso código.

from validate_docbr import CPF

cpf = CPF()
cpf.validate('10044387610') #Ela aceita tanto com máscara quanto sem máscara
cpf.validate('100.443.876-10')

## Capítulo 04 - Utilizando um Pacote
### Vamos agora utilizar a versão mais atualizada da nossa classe com a validação do número do cpf

from CPF import Cpf
cpf1 = '10044387610'
cpf2 = 12345
cpf_dois = 12354367912
cpf_tres = '12354367996'

cpf_um = Cpf(cpf1)
cpf_dois = Cpf(cpf2)

Cpf(cpf_dois)
print(Cpf(cpf_tres))

# Aula 02 - Validando CNPJ e construindo uma factory

## Capitulo 01 - Validando CNPJ

from validate_docbr import CNPJ

cnpj = CNPJ()
cnpj_1 = '35379838000112'
print(cnpj.validate(cnpj_1))

### Vamos testar nosso novo código que pode receber tanto cpf quando cnpj.

from cpf_cnpj import CpfCnpj
cnpj_1 = '35379838000112'
documento_1 = CpfCnpj(cnpj_1,'cnpj')

cnpj_2 = '35379838000142'
documento_2 = CpfCnpj(cnpj_2,'cnpj')

cpf_dois = 12354367912
documento_3 = CpfCnpj(cpf_dois,'cpf')
cpf_tres = 10044387610
documento_4 = CpfCnpj(cpf_tres,'cpf')


##Capítulo 02 - Máscara para CNPJ
### Com os ajustes feitos para incorporar a máscara de cnpj, vamos testar nosso código.
from cpf_cnpj import CpfCnpj

cnpj_1 = '35379838000112'
documento_1 = CpfCnpj(cnpj_1,'cnpj')
print(documento_1)
cnpj_2 = '35379838000142'
documento_2 = CpfCnpj(cnpj_2,'cnpj')

cpf_dois = 12354367912
documento_3 = CpfCnpj(cpf_dois,'cpf')
cpf_tres = 10044387610
documento_4 = CpfCnpj(cpf_tres,'cpf')
print(documento_4)

## Capítulo 03 - Refatorando o código
### Nosso código está praticamente pronto, mas podemos ver que ele está desnecessariamente grande e complexo.
### Para isso, vamos criar uma Factory para que ela decida qual dos métodos utilizar quando fizermos o input do tipo de documento.

from cpf_cnpj import Documento

cnpj_1 = '35379838000112'
documento_1 = Documento.cria_documento(cnpj_1)
print(documento_1)

cpf_tres = '10044387610'
documento_4 = Documento.cria_documento(cpf_tres)
print(documento_4)


# Aula 03 - Validando telefones com expressões regulares
## Capítulo 2 - Definindo padrão para telefones

import re

padrao_molde = "(xx)aaaa-wwww" #Formato que esperando encontrar de um telefones
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}" #Vamos procurar por uma sequencia formada por 2 numeros seguida por 4,5 numeros, seguida por outros 4 numeros

## Testando a busca por padroes
text = "Meu telefone é 31988190639"
resposta = re.findall(padrao,text) #O findall retorna todos as string com aquele padrão que forem encontradas em uma lista
print(resposta)

text2 = "Meu telefone é 31988190639 ou então 3312344321"
resposta2 = re.findall(padrao,text2)
print(resposta2)


### Vamos testar a classe que acabamos de criar
from TelefonesBr import TelefonesBr
telefone = "31988190639"
telefone2 = "12344569"
telefone_objeto = TelefonesBr(telefone)
telefone_objeto2 = TelefonesBr(telefone2)
print(telefone_objeto)

## Capitulo 3 - Criando Máscara para o número de telefone
### Uma das vantagens em utilizar o re, é que além de buscarmos expressões regulares, podemos agrupá-las de modo a ter uma lista com o padrão que desejamos.

from TelefonesBr import TelefonesBr
telefone = "5531988190639"
padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})" #Agora utilizamos os 2 ou 3 digitos para identificar o pais.
resposta = re.findall(padrao,telefone)
print(resposta)
### Pensando em validar apenas telefones brasileiros, vamos ajustar a parte do DDI para pegar apenas 2 digitos.
### Além disso, vamos utilizar o metodo search para buscar o padrão, o que vai nos permitir utilizar o metodo group para retornar os elementos em cada uma das posicoes
resposta_group = re.search(padrao,telefone)
print(resposta_group)
print(resposta_group.group())
print(resposta_group.group(1))
print(resposta_group.group(2))

### Vamos testar a máscara que criamos
from TelefonesBr import TelefonesBr
telefone = "5531988190639"
telefone_objeto = TelefonesBr(telefone)
telefone_objeto
print(telefone_objeto)

# Aula 04 - Manipulando e formatando datas
## Capitulo 01 - Datas no Python

### O python possui uma biblioteca nativa que lida com datas e campos de data, chamada datetime. Duas classes importantes são a datetime e a timedelta.

from datetime import datetime, timedelta

print(datetime.today()) #o método today retorna o momento exato que o comando é rodadao

### Vamos testar a classe que criamos

from datas_br import DatasBr

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())

## Capitulo 02 - Formatando Datas
### Vamos focar agora em formatar como a data é representada.
hoje = datetime.today()
print(hoje)
hoje_formatada = hoje.strftime("%Y") #Retornando apenas o ano
print(hoje_formatada)
hoje_format = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje_format)
print(type(hoje_format))
### Note que ao utlizar o metodo strftime, nos é retornado uma string, ou seja, perdemos nossa capacidade de utilizar os metodos da biblioteca datetime.
### É boa pratica utilizar esta máscara apenas quando formos apresentar esta informação e não realizar nenhuma operação mais com ela.

from datetime import datetime, timedelta
from datas_br import DatasBr
hoje = datetime.today()
cadastro = DatasBr()
print(cadastro)

## Capitulo 03 - Diferença entre datas e timedelta
### Antes de continuarmos, vamos analisar alguns detalhes sobre metodos especiais.
### Vamos olhar para o metodo 'len'

numero = 1
string = "um"
print(len(string)) #Note que para a string, o metodo len roda legal
print(len(numero)) #Já para inteiros, ests não possuem o método especial 'len'

### Este exemplo nos mostra que certos tipos de classes possuem 'metodos especiais' que nos permitem, ou não, utlizar certos métodos.
### Outro exemplo, seria somar dois inteiros.
numero1 = 2
numero2 = 3
print(numero1+numero2)

### Felizmente, a classe datetime possui métodos especiais que nos permitem adicionar e subtrair datas e juntamente com a biblioteca 'timedelta' podemos fazer manipulações com datas.

hoje = datetime.today()
amanha = datetime.today()+timedelta(days=1)

print(amanha-hoje)

### Teste da nossa versão final.
from datas_br import DatasBr
cadastro = DatasBr()
print(cadastro)
print(cadastro.tempo_cadastro())
