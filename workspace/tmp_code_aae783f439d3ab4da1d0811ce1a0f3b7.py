import pandas as pd
import requests

# Fetching historical data for BTC and WLD coins from an API
def get_historical_data():
    url = 'https://min-api.cryptocompare.com/data/v2/histoday'
    
    params_btc = {'fsym': 'BTC',
                  'tsym': 'USD',
                  'limit': 1000}
    
    params_wld = {'fsym': 'WLD',
                  'tsym': 'USD',
                  'limit': 1000}

    btc_resp = requests.get(url, params=params_btc).json()['Data']['Data']
    wld_resp = requests.get(url, params=params_wld).json()['Data']['Data']

    btc_df = pd.DataFrame(btc_resp).set_index('time')
    wld_df = pd.DataFrame(wld_resp).set_index('time')

    return btc_df, wld_df

# Loading historical data from the API into pandas dataframe
btc_df, wld_df = get_historical_data()

# Printing head of the BTC dataframe
print(btc_df.head())