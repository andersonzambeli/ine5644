import pandas as pd
import os as os

estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
atribs = ["cod_mdr","dsc_situacao_contrato_mdr", "dsc_situacao_objeto_mdr","programa",
"acao", "uf_SIGLA_UF", "mun_MUNNOMEX","Código IBGE",
"empreendimento", "situacao_obra", "situacao_obra_base_validacao", "situacao_contrato", "prc_fisico",
"dte_inicio_obra", "dte_fim_obra", "pop_beneficiada", "vlr_investimento", "Populacao", "mun_ALTITUDE", "mun_AREA"]
# Preenche as obras com codigo ibge que falta usando mun_MUNNOMEX e uf_SIGLA_UF e os mesmo campos na base de dados de municipio
# Depois seleciona somente obras com inicio depois de 01/03/2017

input_path = './Data_mining/SIMU_selects/simu_selects6.csv'
input_path2 = './Data_mining/SIMU_selects/simu_ibge_code.csv'
output_path = './Data_mining/SIMU_selects/simu_ibge_code.csv'
output_path2 = './Data_mining/SIMU_selects/simu_clean.csv'
output_path3 = './Data_mining/SIMU_selects/simu_clean_veic.csv'

mun_path = './Municipios/simu_carteira_municipios.csv'
pop_path = './Municipios/simu_carteira_populacao.csv'
veic_path = './Data_mining/SIMU/simu_frota.csv'


df_simu = pd.read_csv(input_path)
df_muni = pd.read_csv(mun_path)
df_pop = pd.read_csv(pop_path)
df_veic = pd.read_csv(veic_path)


# df_pop.info()



tot_item = 0
df_simu = df_simu[df_simu["dte_inicio_obra"] >="2018-01-01"]
df_simu = df_simu[df_simu["dte_fim_obra"] <= "2023-03-01"]

miss = df_simu[df_simu['Código IBGE'].isnull()].index.tolist()
print(len(miss))
# print(miss[0])

for i in miss:

    municipio = df_simu.loc[i,'mun_MUNNOMEX']
    uf = df_simu.loc[i,'uf_SIGLA_UF']

    # print(municipio)
    # print(uf)

    index_mun = df_muni[df_muni['mun_MUNNOMEX'].str.fullmatch(municipio) & df_muni['uf_SIGLA_UF'].str.fullmatch(uf)].index.tolist()
    
    if len(index_mun) == 0:
        continue
    
    else:
        #print(index_mun)

        muni_code = df_muni.loc[index_mun[0], 'Código IBGE']
        muni_alt = df_muni.loc[index_mun[0], 'mun_ALTITUDE']
        muni_area = df_muni.loc[index_mun[0], 'mun_AREA']

        
        #print(muni_code)

        df_simu.loc[i,'Código IBGE'] = muni_code 
        df_simu.loc[i,'mun_ALTITUDE'] = muni_alt
        df_simu.loc[i,'mun_AREA'] = muni_area      
        tot_item = tot_item + 1

print(tot_item)

df_simu = df_simu.dropna(subset=['Código IBGE'])
df_simu = df_simu.dropna(subset=['mun_ALTITUDE'])
df_simu = df_simu.dropna(subset=['mun_AREA'])

df_simu.to_csv(output_path, index=False)

del df_simu

df_simu = pd.read_csv(input_path2)
df_simu.info()
miss = df_simu[df_simu['Populacao'].isnull()].index.tolist()
df_pop = df_pop[df_pop['ano'] == 2020]

for i in miss:

    muni_code = df_simu.loc[i,'Código IBGE']
    index_ = df_pop[df_pop['Código IBGE'] == muni_code].index.tolist()

    pop_tot = df_pop.loc[index_[0], 'Populacao']

    df_simu.loc[i,'Populacao'] = pop_tot


    
    
    

df_simu = df_simu.dropna(subset=['Populacao'])




df_simu.info()


df_simu.to_csv(output_path2, index=False)




