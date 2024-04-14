# filename: collect_data.py
import requests
import pandas as pd

url = 'https://api.pro.coinbase.com'
product_id = 'WLD-USD'
granularity = 3600

# Querying for the last 2 days data as per 3600 seconds time duration
params = {
    'start': pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=2),
    'end': pd.Timestamp.now(tz='UTC'),
    'granularity': granularity
}

response = requests.get(f'{url}/products/{product_id}/candles', params=params)

if response.ok:
    data = pd.DataFrame(response.json(), columns=['time', 'low', 'high', 'open', 'close', 'volume'])
    data['time'] = pd.to_datetime(data['time'], unit='s')
    data.set_index('time', inplace=True)
    data.to_csv(f'{product_id}_{granularity}.csv')
else:
    print(f'Request failed with {response.reason}')