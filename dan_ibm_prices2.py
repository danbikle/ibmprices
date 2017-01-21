# dan_ibm_prices2.py

# This script should
# get IBM prices from a CSV file and calculate the 10-day moving avg for each price and write it to a CSV file.

import pandas as pd

prices0_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=IBM')
prices0_df.to_csv('/tmp/prices0.csv', float_format='%4.2f', index=False)
# Now I should have a CSV file.

prices1_df = pd.read_csv('/tmp/prices0.csv')

prices2_df = prices1_df.copy()[['Date','Adj Close']].sort_values(['Date'])

prices2_df.columns = ['Date','price']

price_ma_sr = prices2_df.rolling(window=10).mean().price.fillna(0)

# Google: In Pandas how to add a series to a DataFrame as a column?
prices2_df['price_ma'] = price_ma_sr

prices3_df = prices2_df.copy()[['Date','price','price_ma']]

prices3_df.to_csv('/tmp/prices_ma.csv', float_format='%4.2f', index=False)
print('Prices and Mvg. Avg. CSV: /tmp/prices_ma.csv')
