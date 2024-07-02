import pandas as pd
import os as os
from csv import QUOTE_NONNUMERIC

estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
atribs = ["cod_mdr","dsc_situacao_contrato_mdr", "dsc_situacao_objeto_mdr","programa",
"acao", "uf_SIGLA_UF", "mun_MUNNOMEX","Código IBGE",
"empreendimento", "situacao_obra", "situacao_obra_base_validacao", "situacao_contrato", "prc_fisico",
"dte_inicio_obra", "dte_fim_obra", "pop_beneficiada", "vlr_investimento", "Populacao", "mun_ALTITUDE", "mun_AREA"]
# Preenche as obras com codigo ibge que falta usando mun_MUNNOMEX e uf_SIGLA_UF e os mesmo campos na base de dados de municipio
# Depois seleciona somente obras com inicio depois de 01/03/2017

input_path = './Data_mining/SIMU_selects/simu_selects6.csv'
input_path2 = './Data_mining/SIMU/simu_com_empreendimento.csv'
output_path = './Data_mining/SIMU_selects/simu_ibge_code.csv'
output_path2 = './Data_mining/SIMU_selects/simu_clean.csv'
output_path3 = './Data_mining/SIMU_selects/simu_com_empreendimento_tot_veic.csv'

mun_path = './Municipios/simu_carteira_municipios.csv'
pop_path = './Municipios/simu_carteira_populacao.csv'
veic_path = './Data_mining/SIMU/simu_frota.csv'


df_simu = pd.read_csv(input_path2, sep=';', quoting=QUOTE_NONNUMERIC)
df_muni = pd.read_csv(mun_path)
df_pop = pd.read_csv(pop_path)
df_veic = pd.read_csv(veic_path)


# df_simu = df_simu.dropna(subset=['Populacao'])


veics = df_veic[df_veic["ano"] == 2020]
veics = veics.dropna(subset=['TOTAL_VEICULOS'])

print(len(df_simu.index))
for i in range(len(df_simu.index)):
    muni_code = df_simu.at[i,'Código IBGE']   
    #muni_code = int(muni_code/10)
    

    index_mun = veics[veics['Código IBGE'] == muni_code].index.tolist()
    #print(len(index_mun))

    if len(index_mun) == 0:
        continue

    else:
        tot_veic = veics.loc[index_mun[0], "TOTAL_VEICULOS"]
        if i == 0:
            print(muni_code)
            print(tot_veic)
            print(index_mun[0])
        
        df_simu.loc[i,'tot_veic'] = tot_veic 

   
    
df_simu = df_simu.dropna(subset=['tot_veic'])
        
df_simu.info()
print(df_simu.shape)


df_simu.to_csv(output_path3, index=False, sep=';', quoting=QUOTE_NONNUMERIC)