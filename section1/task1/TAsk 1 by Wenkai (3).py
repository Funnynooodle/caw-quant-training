#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime


# In[3]:


# up = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=730&toTs=1554094800'
#这个就是正式开始的项目

class ccdata:
    
    def __init__(self, fsym, tsym, limit, toTs ):
        self.fsym =fsym
        self.tsym =tsym
        self.limit = limit
        self.toTs =toTs

    def histohour (self):
        
        up = f'https://min-api.cryptocompare.com/data/v2/histohour?fsym={self.fsym}&tsym={self.tsym}&limit={self.limit}&toTs={self.toTs}'                                                                         
        rep = requests.get(up)
        stp = rep.json()
        dissp = pd.DataFrame(stp['Data']['Data'])
        
        p = dissp['time']
        d=[]

        for i in p.unique():
            f = datetime.fromtimestamp(int(i))
            d.append(f)
        d    

        time_date = pd.DataFrame(d, columns =['time'])
        t = dissp.iloc[:,:7]
        fina = pd.concat([t,time_date], sort= False, axis = 1)
        final = fina.iloc[:,1:]
        final = final[['close','high','low','open','volumefrom', 'volumeto', 'time']]
        final
        return final

    def transsignals(self):
        upt = f'https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym={self.fsym}'
        rept = requests.get(upt)
        stpt = rept.json()
        disspt = pd.DataFrame(stpt['Data'])
        return disspt[disspt.columns[4:]] 

box =[]

for i in [1554094800, 1546894800, 1539694800,  1532494800, 1525294800,
1518094800, 1510894800, 1503694800, 1498280400]:
    
    daata = ccdata('BTC','USD', 2000, i)  
    qe = daata.histohour()
    box.append(qe)

box   


# In[4]:


df = pd.concat(box)
df_sort = df.sort_values(by=['time'],ascending=False)
dr_er = df_sort.drop_duplicates(subset ="time") 
dr_er


# In[7]:


u =daata.histohour()
u.to_csv (r'C:\Users\Owner\Desktop\task1_data1.csv', index = False, header=True)


# In[ ]:





# In[ ]:




