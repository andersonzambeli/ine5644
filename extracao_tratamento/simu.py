import pandas as pd
import os as os

estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
atribs = ["cod_mdr","dsc_situacao_contrato_mdr", "dsc_situacao_objeto_mdr","programa",
"acao", "uf_SIGLA_UF", "mun_MUNNOMEX","Código IBGE",
"empreendimento", "situacao_obra", "situacao_obra_base_validacao", "situacao_contrato", "prc_fisico",
"dte_inicio_obra", "dte_fim_obra", "pop_beneficiada", "vlr_investimento", "Populacao", "mun_ALTITUDE", "mun_AREA"]

path_simu = './Data_mining/SIMU/simu.csv'
output_path = './Data_mining/SIMU_selects/simu_select_col.csv'
df = pd.read_csv(path_simu)
print(df.head())
df1 = df[atribs]
df1.to_csv(output_path,index=False)