# writer: Olebogeng Legotsa
# year: 2025
# database: https://archive.ics.uci.edu/dataset/352/online+retail

import pandas as pd 

df=pd.read_excel('online retail/Online Retail.xlsx', sheet_name='Online Retail')

<<<<<<< HEAD
print(df)
=======
#sum quantity by invoice date
df['InvoiceDate_reformat']=pd.to_datetime(df['InvoiceDate'])
Quantity_Sum=df.groupby(['InvoiceDate_reformat','Description'])['Quantity'].sum().reset_index()

#move quanity sum to new sheet in excel
with pd.ExcelWriter('online retail/Online Retail.xlsx',engine='openpyxl', mode='a',if_sheet_exists='replace') as writer:
    Quantity_Sum.to_excel(writer,sheet_name='Daily Sum',index=False)

print(pd.read_excel('online retail/Online Retail.xlsx', sheet_name='Daily Sum'))


>>>>>>> fc9b8e0 (code changes 20072025)
