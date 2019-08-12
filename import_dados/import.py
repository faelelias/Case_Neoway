#importado base e padronizando separadores


import pandas as pd
dataRaw = pd.read_csv("C:\\Users\\rafael.elias\\Documents\\case\\base_new.csv", sep='\s+',decimal=',',engine='python',skiprows=1,header=None,names=['CPF' ,'PRIVATE' ,'INCOMPLETO' ,'DATA_DA_ULTIMA_COMPRA' ,'TICKET_MEDIO' ,'TICKET_DA_ULTIMA_COMPRA' ,'LOJA_MAIS_FREQUENTE' ,'LOJA_DA_ULTIMA_COMPRA'])
dataRaw.to_csv("C:\\Users\\rafael.elias\\Documents\\case\\base_new2.csv", sep=',',decimal='.', index=False)




print (dataRaw.head(10))