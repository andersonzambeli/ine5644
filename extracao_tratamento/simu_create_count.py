import pandas as pd
import os as os
import time

estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
atribs = ["cod_mdr","dsc_situacao_contrato_mdr", "dsc_situacao_objeto_mdr","programa",
"acao", "uf_SIGLA_UF", "mun_MUNNOMEX","Código IBGE",
"empreendimento", "situacao_obra", "situacao_obra_base_validacao", "situacao_contrato", "prc_fisico",
"dte_inicio_obra", "dte_fim_obra", "pop_beneficiada", "vlr_investimento", "Populacao", "mun_ALTITUDE", "mun_AREA"]
# Preenche e seleciona as obras com codigo ibge

input_path = './Data_mining/SIMU_selects/simu_filter_pop.csv'
input_path2 = './Data_mining/SIMU_selects/simu_dates.csv'
output_path = './Data_mining/SIMU_selects/simu_dates.csv'
output_path2 = './Data_mining/SIMU_selects/simu_counts.csv'

df_simu = pd.read_csv(input_path)

# df_simu.info()df_simu.info()

# print(df_simu.loc[0,'dte_inicio_obra'])
# date = pd.to_datetime(df_simu['dte_inicio_obra']) - pd.to_timedelta(60, unit='d')
# date2 = pd.to_datetime(df_simu['dte_fim_obra']) - pd.to_timedelta(60, unit='d')
# print(date)
# print(date2)

df_simu['dte_antes_60'] = pd.to_datetime(df_simu['dte_inicio_obra']) - pd.to_timedelta(60, unit='d')
df_simu['dte_depois_60'] = pd.to_datetime(df_simu['dte_fim_obra']) + pd.to_timedelta(60, unit='d')
df_simu['dte_antes_180'] = pd.to_datetime(df_simu['dte_inicio_obra']) - pd.to_timedelta(180, unit='d')
df_simu['dte_depois_180'] = pd.to_datetime(df_simu['dte_fim_obra']) + pd.to_timedelta(180, unit='d')
df_simu['dte_antes_365'] = pd.to_datetime(df_simu['dte_inicio_obra']) - pd.to_timedelta(365, unit='d')
df_simu['dte_depois_365'] = pd.to_datetime(df_simu['dte_fim_obra']) + pd.to_timedelta(365, unit='d')

df_simu.info()

df_simu.to_csv(output_path, index=False)

time.sleep(15)

del df_simu

df_simu = pd.read_csv(input_path2)
#df_simu.info()

periodos = [60, 180, 365]

for i in range(len(df_simu.index)):

    uf = df_simu.at[i,'uf_SIGLA_UF']
    muni_code = df_simu.at[i,'Código IBGE']
    # print(muni_code)
    muni_code = int(muni_code/10)
        
    esta_path = './Data_mining/SIH/' + uf + '/tab_SIH_selected_' + uf + '.cvs'

    df_esta = pd.read_csv(esta_path)
    # df_esta.info()

    df_esta = df_esta[df_esta['MUNIC_RES'] == muni_code]
    print('##################################################################\n' + str(i))

    for p in periodos:

    #print('\n\n################################################ Periodo de ' + str(p) + ' dias ####################################################')
    

        


        
        

        data_antes = df_simu.loc[i, str('dte_antes_' + str(p))]
        
        data_inicio = df_simu.loc[i, ('dte_inicio_obra')]
        
        data_fim = df_simu.loc[i, ('dte_fim_obra')]
        
        data_apos = df_simu.loc[i, str('dte_depois_' + str(p))]
        
        cont_antes = len(df_esta[(df_esta['DT_INTER'] >= data_antes) & (df_esta['DT_INTER'] <= data_inicio)])
        
        cont_depois = len(df_esta[(df_esta['DT_INTER'] >= data_fim) & (df_esta['DT_INTER'] <= data_apos)])

        # print(muni_code)
        # df_esta.info()
        # print('\nAntes: ', data_antes)
        # print('Inicio: ', data_inicio)
        # print('Fim: ',data_fim)
        # print('Apos: ', data_apos)
        # antes = df_esta[(df_esta['DT_INTER'] >= data_antes) & (df_esta['DT_INTER'] <= data_inicio)]
        # print('Antes: ', antes)
        # depois = df_esta[(df_esta['DT_INTER'] >= data_fim) & (df_esta['DT_INTER'] <= data_apos)]
        # print('Depois: ', depois)

        df_simu.at[i, str('cont_antes_' + str(p))] = cont_antes
        df_simu.at[i, str('cont_depois_' + str(p))] = cont_depois
    
    del df_esta
    
df_simu.info()
df_simu.to_csv(output_path2, index=False)

del df_simu
    






