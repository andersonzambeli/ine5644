# Extração em 2 de julho de 2024
from pysus.ftp.databases.sih import SIH
import pandas as pd
import os as os

estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
# estados1 = ['AC','AL','AP','AM']
# estados1 = ['BA','CE','DF','ES']
# estados1 = ['GO','MA','MT','MS']
# estados1 = ['MG','PA','PB','PR']
# estados1 = ['PE','PI','RJ','RN']
# estados1 = ['RS','RO','RR','SC']
estados1 = ['SP','SE','TO']



sih = SIH().load() # Loads the files from DATASUS
print(sih.metadata)

for uf_ in estados1:

    dir_ = './SIH/'+ uf_ + '/'
    tab = sih.download(sih.get_files('RD', uf=uf_ ,year=[2017,2018,2019,2020,2021,2022,2023,2024]), local_dir= dir_)
    del tab

# db1 = pd.read_parquet('./SIH/RDSC2305.parquet')
# print(db1.head())

# db2 = pd.read_parquet('./SIH/RDSC2304.parquet')
# print(db2.head())


# db.to_csv(path_or_buf="./sih_sp.cvs")
# for col_name in db.columns:
#     print(col_name)


# select_atb = db[["MUNIC_RES","CNES","CID_NOTIF", "DT_INTER","DT_SAIDA","DIAG_PRINC", "MORTE", "MARCA_UTI", "UTI_MES_IN", "UTI_MES_AN", "UTI_MES_AL", 'UTI_MES_TO', 'VAL_TOT', 'VAL_UTI']]
# select_atb = select_atb.loc[select_atb['MARCA_UTI'] != '00']
# print(select_atb.head())
# #print(select_atb.info())
# select_atb.to_csv(path_or_buf="./select_atbs.cvs")


# print(select_atb.loc[select_atb['MUNIC_RES'] == '420540'])
# #print(db.columns.tolist())