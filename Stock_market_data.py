'''
1) Obtain historical stock prices for a specific company or index (such as the S&P 500) 
using an API or web scraping.

2) Clean and preprocess the data, removing any missing values or outliers.

3) Calculate basic statistics such as daily returns, volatility, and correlations between
 different stocks or indices.

4) Create visualizations such as line charts, candlestick charts, or heatmaps to help you 
identify trends and patterns in the data.

5) Apply machine learning techniques such as regression or clustering to predict future 
stock prices or identify similar stocks based on their historical performance.
'''

import requests
import pandas as pd

# Specify API endpoint and parameters
url = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'TSLA',
    'outputsize': 'full',
    'apikey': 'TE1E1KD330UYLRHQ'
}

# Make API request and retrieve data
response = requests.get(url, params=params)
data = response.json()

# Convert data to Pandas DataFrame
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
df = df.astype(float)
df.index = pd.to_datetime(df.index)

# Print the first 5 rows of the DataFrame
print(df.head())
