#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import pandas as pd
import numpy as np
import seaborn as sns


# In[ ]:


# r = requests.get('https://api.github.com/events')
# r = requests.put('https://httpbin.org/put', data = {'key':'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')


# In[8]:


r = requests.get('https://min-api.cryptocompare.com/documentation?key=Historical&cat=dataHistohour')
# https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=10


# In[11]:


print(dir(r))


# In[12]:


print(help(r))


# In[13]:


print(r.text)


# In[14]:


print(r.content)


# In[ ]:





# In[9]:


r = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=10')


# In[10]:


p = r.text


# In[11]:


q = r.json()
# f = requests.get(url)
# ipdata = f.json()
# df = pd.DataFrame(ipdata['Data'])


# In[12]:


q


# In[13]:


q.items()


# In[14]:


type(q)


# In[15]:


df = pd.DataFrame(q['Data']['Data'])
df


# In[83]:


url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=2000&toTs=1491022800'


# In[84]:


# payload = {'fsym': 'BTC', 'tsym': 'USD','start_time':'2017-04-01', 'end_time':'2020-04-01','e':'binance'}
re = requests.get(url)
# 'start_time':"2017-04-01", 'end_time':"2020-04-01",


# In[85]:


st = re.json()
st


# In[86]:


diss = pd.DataFrame(st['Data']['Data'])


# In[87]:


diss


# In[88]:


p


# In[89]:


# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2017, 1, 11)

# df = web.DataReader("AAPL", 'yahoo', start, end)
# df.tail()


# In[137]:


pd.to_datetime(1491004800, unit='s')


# In[123]:


from datetime import datetime
import time

dt = datetime.strptime('2019-04-01 00:00:00', '%Y-%m-%d %H:%M:%S')
ts = time.mktime(dt.timetuple())


# In[124]:


ts


# In[172]:


# 练习

def func_sss( i, j ,k, p):
    up = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={i}&tsym={j}&limit={k}&toTs={p}'
    rep = requests.get(up)
    stp = rep.json()
    dissp = pd.DataFrame(stp['Data']['Data'])
    return dissp    


# In[173]:


pt = func_sss('BTC','USD',730,1554094800)


# In[175]:


pt


# In[ ]:





# In[132]:


up = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=730&toTs=1554094800'


# In[133]:


rep = requests.get(up)


# In[134]:


stp = rep.json()
stp


# In[164]:


dissp = pd.DataFrame(stp['Data']['Data'])


# In[165]:


dissp


# In[ ]:





# In[ ]:





# In[ ]:


up = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=730&toTs=1554094800'
rep = requests.get(up)
stp = rep.json()
dissp = pd.DataFrame(stp['Data']['Data'])
dissp


# In[ ]:


class ccdata: 
    


# In[ ]:





# In[147]:


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(5,56666)
# x.r, x.i
# (3.0, -4.5)


# In[148]:


x.r


# In[ ]:


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'


# In[ ]:


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']


# In[ ]:


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# In[ ]:


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# In[ ]:





class pic:
    
up = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=730&toTs=1554094800'
def dfd(self, fsym, tsym, limit, toTs ): 
    self.fsym =fsym
    self.tsym =tsym
    self.limit = limit
    self.toTs =toTs
    up = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym={}&limit={}&toTs={}'.format('fsym','tsym',limit,toTs)
    rep = requests.get(up)
    stp = rep.json()
    dissp = pd.DataFrame(stp['Data']['Data'])

dissp


# In[ ]:





# In[150]:


upt = 'https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym=BTC'
#     rept = requests.get(upt)
#     stpt = rept.json()
#     disspt = pd.DataFrame(stpt['Data']['Data'])

# disspt


# In[151]:


rept = requests.get(upt)
stpt = rept.json()


# In[152]:


stpt


# In[155]:


disspt = pd.DataFrame(stpt['Data'])
disspt[disspt.columns[4:]] 


# In[180]:


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
        return dissp

    def transsignals(self):
        upt = f'https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym={self.fsym}'
        rept = requests.get(upt)
        stpt = rept.json()
        disspt = pd.DataFrame(stpt['Data'])
        return disspt[disspt.columns[4:]] 
    
daata = ccdata('BTC','USD', 730, 1554094800)   
daata.histohour()
# daata.transsignals()


# In[ ]:





# In[161]:


def histohour (fsym, tsym,limit,toTs):
       
       up = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym={}&tsym={}&limit={}&toTs={}'.format('fsym','tsym',
                                                                                                     limit,toTs)
                                                                                             
       rep = requests.get(up)
       stp = rep.json()
       dissp = pd.DataFrame(stp['Data']['Data'])
       return dissp


# In[176]:


def histohour (ffsym, ttsym, llimit, ttoTs):
    up = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={ffsym}&tsym={ttsym}&limit={llimit}&toTs={ttoTs}'                                                                         
    rep = requests.get(up)
    stp = rep.json()
    dissp = pd.DataFrame(stp['Data']['Data'])
    return dissp


# In[177]:


histohour('BTC','USD', 730, 1554094800)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[162]:


pppp = histohour('BTC','USD', 730, 1554094800)


# In[ ]:





# In[ ]:


upt = 'https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym=BTC'
rept = requests.get(upt)
stpt = rept.json()
disspt = pd.DataFrame(stpt['Data'])
disspt[disspt.columns[4:]] 


# In[ ]:


def __init__(mysillyobject, name, age):
  mysillyobject.name = name
  mysillyobject.age = age


# In[ ]:


class ccdata:
    
    def __init__ (self, )


# In[ ]:


# Parent and child class

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# In[ ]:





# In[ ]:





# In[138]:


ll ='https://min-api.cryptocompare.com/data/'
jj ='v2/histoday?fsym=BTC&tsym=USD&limit=730&toTs=1554094800'


# In[140]:


qq =ll+jj
qq


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[195]:


# import plotly as py
# plotly.offline.init_notebook_mode(connected=True)


# In[ ]:





# In[56]:


import datetime
import plotly.offline as py
import plotly.graph_objs as go
import pandas_datareader as web

start = datetime.datetime(2014,1,1)
end = datetime.datetime(2018,1,1)

FB = web.DataReader('FB','yahoo',start,end)
TW = web.DataReader('TWTR','yahoo',start,end)
AAPL = web.DataReader('AAPL','yahoo',start,end)

trace = go.Ohlc(
    x=FB.index[:],
    open=FB['Open'],
    high=FB['High'],
    low=FB['Low'],
    close=FB['Close'],
    name='FB',
    increasing=dict(line=dict(color= 'blue')),
    decreasing=dict(line=dict(color= 'red'))
)

trace2 = go.Ohlc(
    x=TW.index[:],
    open=TW['Open'],
    high=TW['High'],
    low=TW['Low'],
    close=TW['Close'],
    name='TW',
    increasing=dict(line=dict(color= 'yellow')),
    decreasing=dict(line=dict(color= 'red'))
)

trace3 = go.Ohlc(
    x=FB.index[:],
    open=AAPL['Open'],
    high=AAPL['High'],
    low=AAPL['Low'],
    close=AAPL['Close'],
    name='AAPL',
    increasing=dict(line=dict(color= 'green')),
    decreasing=dict(line=dict(color= 'red'))
)


data = [trace, trace2, trace3]
layout ={
    'title':'facebook vs Tweeter vs Apple',
    'yaxis': {'title':'price per stock'}
    
}

fig = dict(data=data, layout = layout)
# py.plot = (fig, filename ='stocks.html')
plot_url = py.plot(fig, filename='techstocks.html')
plot_url




# In[ ]:





# In[192]:


# RDS_A = web.DataReader('RDS.A','yahoo',start,end)
XOM= web.DataReader('XOM','yahoo',start,end)
# TOT = web.DataReader('TOT','yahoo',start,end)
xomstock = go.Ohlc(
    x=XOM.index[:],
    open=XOM['Open'],
    high=XOM['High'],
    low=XOM['Low'],
    close=XOM['Close'],
    name='XOM',
    increasing=dict(line=dict(color= 'green')),
    decreasing=dict(line=dict(color= 'red'))
)

layout ={
    'title':'EXX',
    'yaxis': {'title':'price per stock'}
    
}

figg= dict(data = xomstock, layout = layout)
url_xom = py.plot(figg, filename = 'Exxmobil.html')
url_xom


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()


# In[ ]:





# In[ ]:





# In[5]:


from binance.client import Client
# client = Client(api_key, api_secret)
client = Client()
# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# place a test market buy order, to place an actual order use the create_order function
order = client.create_test_order(
    symbol='BNBBTC',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)

# get all symbol prices
prices = client.get_all_tickers()

# withdraw 100 ETH
# check docs for assumptions around withdrawals
from binance.exceptions import BinanceAPIException, BinanceWithdrawException
try:
    result = client.withdraw(
        asset='ETH',
        address='<eth_address>',
        amount=100)
except BinanceAPIException as e:
    print(e)
except BinanceWithdrawException as e:
    print(e)
else:
    print("Success")

# fetch list of withdrawals
withdraws = client.get_withdraw_history()

# fetch list of ETH withdrawals
eth_withdraws = client.get_withdraw_history(asset='ETH')

# get a deposit address for BTC
address = client.get_deposit_address(asset='BTC')

# start aggregated trade websocket for BNBBTC
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()

# get historical kline data from any date range

# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

# fetch weekly klines since it listed
klines = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[117]:


api_key = 's2ComyyRHzzauO9ItDjauLpTMDeEynFQuZlerdXjddt1r1TeFxnt2N6CvYperWZJ' 
api_secret = 'QcSTf2KhoBDq5xjrrQDPgD76nhsK0kHw3opkhRDK7rg2xDIeBIJ7w0xfFTl0VCb6' 


# In[15]:


import pandas as pd


# In[111]:


# To begin here 

from binance.client import Client
from datetime import datetime


def binance_price():
    
    client = Client(api_key, api_secret)

    prices = client.get_all_tickers()

    candles = client.get_klines(symbol='ETHBTC', interval=Client.KLINE_INTERVAL_15MINUTE)

    hcandle = pd.DataFrame(candles)

    hcandle

    hcandle_times = hcandle[0]

    final_time=[]

    for hcandletime in hcandle_times.unique():
        normal_time = datetime.fromtimestamp(int(hcandletime/1000))
        final_time.append(normal_time)

    hcandle.pop(0)
    hcandle.pop(2)
    hcandle.pop(3)
    hcandle.pop(4)
    hcandle.pop(5)
    hcandle.pop(6)
    hcandle.pop(7)
    hcandle.pop(8)
    hcandle.pop(9)
    hcandle.pop(11)

    # after_hcandle=hcandle.rename(columns={'1': 'First column', '9':'ninth column'})
    df_final_time = pd.DataFrame(final_time)
    df_final_time.columns = ['Date']

    new_added_time = df_final_time.join(hcandle)
    final_added_time =new_added_time.rename(columns ={1: 'First column', 10:'tenth column'})
    return final_added_time

print(binance_price())    


# In[150]:


prices = client.get_all_tickers()
pd.DataFrame(prices)


# In[175]:


from binance.client import Client
from datetime import datetime

def market_depth():
    
    client = Client(api_key, api_secret)

    depth = client.get_order_book(symbol='BNBETH')

    df_depth = pd.DataFrame(depth)

    return df_depth 

print(market_depth())

    # depth_id = df_depth.iloc[:,0:1]

    # depth_id


# In[188]:


# fetch 30 minute klines for the last month of 2017


klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

dtt = pd.DataFrame(klines)
dttime = dtt.iloc[:10,0]
dttime

changed_time=[]

for i in dttime:
    timed = datetime.fromtimestamp(int(i/1000))
    changed_time.append(timed)
    
pct = pd.DataFrame(changed_time)
pctn = pct.rename(columns={0:'Date'})
pctn


# In[177]:


type(klines)


# In[ ]:





# In[ ]:


agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')

# iterate over the trade iterator
for trade in agg_trades:
    print(trade)
    # do something with the trade data

# convert the iterator to a list
# note: generators can only be iterated over once so we need to call it again
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', '30 minutes ago UTC')
agg_trade_list = list(agg_trades)

# example using last_id value
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', last_id=23380478)
agg_trade_list = list(agg_trades)


# In[ ]:





# In[ ]:





# In[ ]:





# In[109]:


from binance.client import Client
from datetime import datetime


client = Client(api_key, api_secret)

prices = client.get_all_tickers()

candles = client.get_klines(symbol='ETHBTC', interval=Client.KLINE_INTERVAL_15MINUTE)

hcandle = pd.DataFrame(candles)

hcandle.loc[0:4,1:5]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[103]:


# Practice 
import pandas as pd
import numpy as np
np.random.seed(5)
df = pd.DataFrame(np.random.randint(100, size=(100, 4)), 
                  columns=list('abcd'), 
                  index=['Check{}'.format(i) for i in range(100)])
df.head()


# In[ ]:





# In[ ]:





# In[20]:


# Alternative: 
for price in prices:
    print(price)


# In[22]:


# candles = client.get_klines(symbol='ETHBTC', interval=Client.KLINE_INTERVAL_15MINUTE)


# In[28]:


# candle = pd.DataFrame(candles)
# candle


# In[ ]:




