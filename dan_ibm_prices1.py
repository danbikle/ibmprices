# dan_ibm_prices1.py

# This script should download IBM prices from Yahoo into a DataFrame.

# Then it should write the DataFrame to a CSV file.

# Next, it should get prices from the CSV file and plot them as a time-series into a PNG file.

import pandas as pd
import matplotlib.pyplot as plt

prices0_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=IBM')
prices0_df.to_csv('/tmp/prices0.csv', float_format='%4.2f', index=False)
# Now I should have a CSV file.

prices1_df = pd.read_csv('/tmp/prices0.csv')

prices2_df = prices1_df.copy()[['Date','Adj Close']].sort_values(['Date'])

prices2_df.columns = ['date_s','IBM Adj Closing Price']

# I should create a series of dates from the 'date_s' column of strings:
# Google: In Python how to create a date from a string?

# Demo from py4.us class01 lab:
from datetime import datetime
my_s  = '2016-12-01 13:59:59'
my_dt = datetime.strptime(my_s, '%Y-%m-%d %H:%M:%S')

# I should learn from the above demo:
date_dt_l = [datetime.strptime(day_s, '%Y-%m-%d') for day_s in prices2_df.date_s]

# Google: In Python Pandas how to add a List to a DataFrame as a column?
prices2_df['Date'] = date_dt_l

prices3_df = prices2_df.copy()[['Date','IBM Adj Closing Price']]
prices4_df = prices3_df.set_index('Date')

# I should plot:
prices4_df.plot.line(title="My Plot")
#plt.show()
plt.savefig('dan_ibm_prices1.png')
print('I should have a new plot now: dan_ibm_prices1.png')
