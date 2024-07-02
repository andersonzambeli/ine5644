import pandas as pd
import os as os
from csv import QUOTE_NONNUMERIC

estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
atribs = ["cod_mdr","dsc_situacao_contrato_mdr", "dsc_situacao_objeto_mdr","programa",
"acao", "uf_SIGLA_UF", "mun_MUNNOMEX","Código IBGE",
"empreendimento", "situacao_obra", "situacao_obra_base_validacao", "situacao_contrato", "prc_fisico",
"dte_inicio_obra", "dte_fim_obra", "pop_beneficiada", "vlr_investimento", "Populacao", "mun_ALTITUDE", "mun_AREA"]
# Preenche e seleciona as obras com codigo ibge

input_path = './Data_mining/SIMU_selects/simu_counts.csv'
output_path = './Data_mining/SIMU_selects/simu_final.csv'


df_simu = pd.read_csv(input_path)
df_simu.info()

print(df_simu.columns)

periods = [60, 180, 365]
for p in periods:
    df_simu[('razao_antes_depois_' + str(p))] = df_simu[('cont_antes_' + str(p))].div(df_simu[('cont_depois_' + str(p))], axis=0)
    df_simu[('diferenca_antes_depois_' + str(p))] = df_simu[('cont_antes_' + str(p))] - df_simu[('cont_depois_' + str(p))]


# periodos = [60, 180, 365]
# for p in periodos:
#     df_simu.rename(columns={str('\ncont_antes_' + str(p)) : str('cont_antes_' + str(p)) })

df_simu.info()

df_simu.to_csv(output_path,index=False, sep=';', quoting=QUOTE_NONNUMERIC)