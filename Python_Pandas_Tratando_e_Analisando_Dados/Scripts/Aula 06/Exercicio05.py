import pandas as pd

imoveis = pd.DataFrame([['Apartamento', None, 970, 68],
                        ['Apartamento', 2000, 878, 112],
                        ['Casa', 5000, None, 500],
                        ['Apartamento', None, 1010, 170],
                        ['Apartamento', 1500, 850, None],
                        ['Casa', None, None, None],
                        ['Apartamento', 2000, 878, None],
                        ['Apartamento', 1550, None, 228],
                        ['Apartamento', 2500, 880, 195]],
                        columns = ['Tipo', 'Valor', 'Condominio', 'IPTU'])

imoveis
# Alternativa 1: Elimina os registros que não apresentam a variável Valor
# Correta

imoveis.dropna(subset = ['Valor'])

# Alternativa 2: Elimina os imóveis do tipo Apartamento que não apresentam valor Condominio:

selecao_2 = (imoveis['Tipo'] == 'Apartamento') & (imoveis['Condominio'].isnull())
imoveis[selecao_2]
imoveis
