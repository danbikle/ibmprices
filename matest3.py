# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 19:48:38 2017

@author: Steve Siegel
"""

import pandas as pd


#read Yahoo prices for IBM
ibm_prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=IBM')

#Specify the time frame for prices
start = ibm_prices_df.Date > '2016-12-1' 
stop = ibm_prices_df.Date < '2017-1-1'
pred_sr = start & stop

prices0_df = ibm_prices_df.copy()[['Date','Adj Close']][pred_sr]




prices1_df = prices0_df.sort_values('Date')

prices2_df = prices1_df.set_index('Date')

#IBM prices and date columns
ibm_price = prices1_df['Adj Close']
ibm_dates = prices1_df['Date']

#Calculate IBM 10-day moving average
ibm_price_ma = ibm_price.rolling(center=False,window=10).mean()

#place results in data frame format
data_df = pd.DataFrame({'IBM_Prices':ibm_price,'Moving_AVG':ibm_price_ma})

#Write to csv file
data_df.to_csv('/tmp/moving_avg_IBM.csv',float_format='%4.2f', index=False)

