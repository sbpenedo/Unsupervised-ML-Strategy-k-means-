import pandas as pd
import numpy as np
import datetime as dt 
import yfinance as yf
import pandas_ta as ta
import warnings
import urllib.request
warnings.filterwarnings('ignore')

### Acess wikipedia page and get table of companies
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

# Define the User-Agent header to access wikipedia 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

# Create a request object with the URL and the headers
req = urllib.request.Request(url=url, headers=headers)

# Fetch the raw HTML with urllib
with urllib.request.urlopen(req) as response:
    html = response.read()

# Parse the tables from the HTML
list_of_tables = pd.read_html(html)

# Select the first table
sp500_table = list_of_tables[0]

# Checkpoint
print("S&P 500 Companies Table:")
print(sp500_table.head())

# Some symbols have '.' which need to be changed to '-'
sp500_table['Symbol'] = sp500_table['Symbol'].str.replace('.', '-', regex=False)

symbols_list = sp500_table['Symbol'].unique().tolist()

# Check we have correct list of symbols
print(symbols_list)
print('-' * 30)
print()

# Make end date today
end_date = pd.Timestamp.now().strftime('%Y-%m-%d')

# Make start date 8 years before end date
start_date = pd.to_datetime(end_date) - pd.DateOffset(365 * 8)

# Checkpoint
print('Your start date is:', start_date)
print('Your end date is:', end_date)
print()

# Download data for companies
df = yf.download(
    tickers=symbols_list,
    start=start_date,
    end=end_date,
    auto_adjust=False # Ensure we download adj close
).stack()

df.index.names = ['date', 'ticker']
df.columns = df.columns.str.lower()

# Checkpoint
print(df)

# Save new df as .csv so that this project isn't slow 
df.to_csv('sp500_data.csv')
print("\nData saved to sp500_data.csv")
