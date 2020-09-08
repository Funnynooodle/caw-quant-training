#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime


# In[4]:


# up = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=730&toTs=1554094800'


class ccdata:
    
    def __init__(self, fsym, tsym, limit, toTs ):
        self.fsym =fsym
        self.tsym =tsym
        self.limit = limit
        self.toTs =toTs

    def histohour (self):
        
        up = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={self.fsym}&tsym={self.tsym}&limit={self.limit}&toTs={self.toTs}'                                                                         
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
    
daata = ccdata('BTC','USD', 730, 1554181200)   
daata.histohour()
# daata.transsignals()

