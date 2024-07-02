import pandas as pd
import os as os

# Seleciona todas obras que tem dte_inicio_obra preenchido 


estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
atribs = ["cod_mdr","dsc_situacao_contrato_mdr", "dsc_situacao_objeto_mdr","programa",
"acao", "uf_SIGLA_UF", "mun_MUNNOMEX","Código IBGE",
"empreendimento", "situacao_obra", "situacao_obra_base_validacao", "situacao_contrato", "prc_fisico",
"dte_inicio_obra", "dte_fim_obra", "pop_beneficiada", "vlr_investimento", "Populacao", "mun_ALTITUDE", "mun_AREA"]

input_path = './Data_mining/SIMU_selects/simu_selects2.csv'
output_path = './Data_mining/SIMU_selects/simu_selects3.csv'
df = pd.read_csv(input_path)



df1 = df.dropna(subset=['dte_inicio_obra'])
df1.to_csv(output_path,index=False)