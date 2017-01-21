# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:36:50 2017

@author: Steve Siegel
"""

import pandas as pd
import matplotlib.pyplot as plt


ibm_prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=IBM')

start = ibm_prices_df.Date > '2016-12-1' 
stop = ibm_prices_df.Date < '2017-1-1'
pred_sr = start & stop

prices0_df = ibm_prices_df.copy()[['Date','Adj Close']][pred_sr]


prices1_df = prices0_df.sort_values('Date')

prices2_df = prices1_df.set_index('Date')
ibm_price = prices1_df['Adj Close']
ibm_dates = prices1_df['Date']

ibm_price_ma = ibm_price.rolling(center=False,window=10).mean()

plt.plot(ibm_price,'r',ibm_price_ma,'b')


plt.title("IBM Prices MA")

plt.savefig('IBM_Prices_MA.png')