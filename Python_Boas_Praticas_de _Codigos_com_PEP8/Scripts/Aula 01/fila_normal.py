# Descobrindo o PEP-8 e o TypeHints

## Começando com o TypeHints
### O TypeHints, como o proprio nome sugere, ele dá uma dica de qual o tipo daquela variável em questão.
### Utilizamos da seguinte maneira ->   var:vartype


## Aqui vamos gerar a fila Normal
class filanormal:
    codigo:int = 0    #Estamos dizendo que 'codigo' é uma variável do tipo 'int'.
    fila = []
    clientesatendidos = []
    senhatual:str = ''    #Estamos dizendo que 'senhatual' é do tipo 'string'

    def gerasenhaatual(self)->None: #Estamos dizendo que esse metodo não retorna nada
        self.senhatual = f'NM{self.codigo}'

    def resetafila(self)->None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo +=1

    def atualizafila(self)->None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhatual)

    def chamacliente(self, caixa:int)->str:  #Estamos dizendo que este método retorna uma string e dizendo que a variável 'caixa' recebe um 'int'.
        cliente_atual:str = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return(f'Cliente Atual: {cliente_atual}, dirija-se ao Caixa : {caixa}')
