import pandas as pd
import os as os

estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
atribs = ['N_AIH', 'DT_INTER', 'COBRANCA', 'MUNIC_RES', 'MUNIC_MOV']

for uf in estados:
    path_file = './Data_mining/SIH/' + uf + '/tab_SIH_selected_' + uf + '.cvs'
    df = pd.read_csv(path_file)
    df['DT_INTER'] = pd.to_datetime(df['DT_INTER'], format = '%Y%m%d')
    print(df.head())
    df = df.to_csv(path_file)
   