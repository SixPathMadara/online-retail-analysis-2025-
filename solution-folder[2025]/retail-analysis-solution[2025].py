# writer: Olebogeng Legotsa
# year: 2025
# database: https://archive.ics.uci.edu/dataset/352/online+retail

import pandas as pd 

df=pd.read_excel('online retail/Online Retail.xlsx',sheet_name='Online Retail')

#print(df)
#sum quantity by invoice date
df['InvoiceDate_reformat']=pd.to_datetime(df['InvoiceDate'])
#Group by Daily quantity
Daily_Quantity_Sum=df.groupby([pd.Grouper(key='InvoiceDate_reformat',freq='D'),'Description'])['Quantity'].sum().reset_index()
#Group by weekly quantity
Weekly_Quantity_Sum=df.groupby([pd.Grouper(key='InvoiceDate_reformat',freq='W'),'Description'])['Quantity'].sum().reset_index()
#Group by Monthly quantity
Monthly_Quantity_Sum=df.groupby([pd.Grouper(key='InvoiceDate_reformat',freq='ME'),'Description'])['Quantity'].sum().reset_index()

#move quanity sum to new sheet in excel
with pd.ExcelWriter('online retail/Online Retail.xlsx',engine='openpyxl', mode='a',if_sheet_exists='replace') as writer:
    Daily_Quantity_Sum.to_excel(writer,sheet_name='Daily Sum',index=False)
    Weekly_Quantity_Sum.to_excel(writer,sheet_name='Weekly Sum',index=False)
    Monthly_Quantity_Sum.to_excel(writer,sheet_name='Monthly Sum',index=False)



print(Daily_Quantity_Sum)
print(Weekly_Quantity_Sum)
print(Monthly_Quantity_Sum)


