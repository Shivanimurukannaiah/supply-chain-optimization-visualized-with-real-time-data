
import streamlit as st
from src.loader import load_delivery_data
from src.analyzer import basic_statistics
from src.predictor import prepare_prophet_data, forecast_delays

st.title("🚚 Supply Chain Optimization Dashboard")

df = load_delivery_data("data/delivery_data.csv")
st.write("### Delivery Data Preview", df.head())

if st.button("Show Summary"):
    stats = basic_statistics(df)
    st.write("### Summary Statistics", stats)

if st.button("Forecast Delays"):
    prophet_data = prepare_prophet_data(df)
    forecast = forecast_delays(prophet_data)
    st.write("### Delay Forecast", forecast.tail())
