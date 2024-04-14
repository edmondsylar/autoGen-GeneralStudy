# filename: make_prediction.py
from fbprophet import Prophet
import pandas as pd

# Loading WLD/USD price data from CSV file
data = pd.read_csv('WLD-USD_3600.csv', parse_dates=True, index_col=0)

# Converting data to processable format 
price_data = data['close'].rename('y').reset_index()
price_data.rename(columns={'time': 'ds'}, inplace=True)

# Training the model and getting future dates to make predictions
model = Prophet(yearly_seasonality=True, daily_seasonality=True)
model.fit(price_data)
future = model.make_future_dataframe(periods=2, freq='D')
forecast = model.predict(future)

# Printing the future predictions
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(2))