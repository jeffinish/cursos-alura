# Neste arquivo, vamos utilizar a convenção PEP-8 para formatar nosso código e torná-lo mais facil de ser compreendido.

class FilaPrioritaria:  #Classes utilizam letras maiusculas
    codigo:int = 0
    fila = []
    clientes_atendidos = [] #Variáveis são separadas por _
    senha_atual:str = ''

    def gera_senha_atual(self)->None:
        self.senha_atual = f'PR{self.codigo}'

    def reseta_fila(self)->None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self)->None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa:int)->str:  #Estamos dizendo que este método retorna uma string e dizendo que a variável 'caixa' recebe um 'int'.
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente Atual: {cliente_atual}, dirija-se ao Caixa : {caixa}')

    def estatistica(self, dia:str, agencia:int, flag:str)->dict:    #Retorna um dicionario
        if flag !='detail': #Se a flag NÃO for 'detail', retorna estatística simples
            estatistica = {f'{agencia}-{dia}':len(self.clientes_atendidos)}
        else: #Se a flag for 'detail', retorna um dicionario com informações detalhadas.
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_clientes_atendidos'] = len(self.clientes_atendidos)

        return estatistica
