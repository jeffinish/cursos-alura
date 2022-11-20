from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        mes_cadastro = self.momento_cadastro.month # A biblioteca datetime tem o método 'month' que retorna pra gente o mes da data em questao.
        return mes_cadastro

    def dia_semana(self):
        dia_semana = self.momento_cadastro.weekday() # A biblioteca datetime tem o método 'weekday' que retorna pra gente o dia da semana da data em questao.
        return dia_semana

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today()-self.momento_cadastro
        return tempo_cadastro
