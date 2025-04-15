
from prophet import Prophet
import pandas as pd

def prepare_prophet_data(df):
    df = df[['date', 'delay_minutes']].rename(columns={'date': 'ds', 'delay_minutes': 'y'})
    return df

def forecast_delays(df):
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
