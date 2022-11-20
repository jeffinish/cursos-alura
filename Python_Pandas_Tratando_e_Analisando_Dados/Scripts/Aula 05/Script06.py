import pandas as pd
alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'],
                        'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'],
                        'Idade': [15, 27, 56, 32, 42, 21, 19, 35],
                        'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6],
                        'Aprovado': [True, False, False, True, True, True, False, False]},columns = ['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

selecao = alunos['Aprovado'] == False
reprovados = alunos.loc[selecao, ['Nome', 'Sexo', 'Idade']]
reprovados
