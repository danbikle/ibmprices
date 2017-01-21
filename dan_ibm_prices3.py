# dan_ibm_prices3.py

# This script should
# plot IBM prices and 10-day moving avg into a PNG file.

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

prices0_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=IBM')
prices0_df.to_csv('/tmp/prices0.csv', float_format='%4.2f', index=False)
# Now I should have a CSV file.

prices1_df = pd.read_csv('/tmp/prices0.csv')

prices2_df = prices1_df.copy()[['Date','Adj Close']].sort_values(['Date'])

prices2_df.columns = ['date_s','price']

price_ma_sr = prices2_df.rolling(window=10).mean().price.fillna(0)

prices2_df['price_ma'] = price_ma_sr

prices3_df = prices2_df.copy()[['date_s','price','price_ma']]

date_dt_l = [datetime.strptime(day_s, '%Y-%m-%d') for day_s in prices3_df.date_s]

prices3_df['Date'] = date_dt_l

prices4_df = prices3_df.copy()[['Date','price','price_ma']]
prices5_df = prices4_df.set_index('Date')

# I should plot:
prices5_df.plot.line(title="My Plot")
#plt.show()
plt.savefig('dan_ibm_prices3.png')
print('I should have a new plot now: dan_ibm_prices3.png')

# It is hard to see the mvg avg in above plot.
# I should plot a shorter duration:
gt20161_sr = (prices5_df.index > datetime.strptime('2016-01-01', '%Y-%m-%d'))
gt20162_sr = (prices5_df.index < datetime.strptime('2016-06-01', '%Y-%m-%d'))
gt2016_sr  = (gt20161_sr & gt20162_sr)

prices5_df[gt2016_sr].plot.line(title="IBM")

plt.savefig('dan_ibm_prices4.png')
print('I should have a new plot now: dan_ibm_prices4.png')
