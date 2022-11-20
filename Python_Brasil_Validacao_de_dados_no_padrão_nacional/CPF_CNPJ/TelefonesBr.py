import re

class TelefonesBr:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número Incorreto")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self,telefone):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})" #Agora utilizamos os 2 digitos para identificar o codigo do pais, uma vez que estamos considerando apenas telefones brasileiros.
        reposta = re.findall(padrao,telefone)
        if reposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado
