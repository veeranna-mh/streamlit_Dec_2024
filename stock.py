import streamlit as st
import yfinance as yf
import datetime

st.title("Stock market analyser - Veeranna")

ticker_data=yf.Ticker("MSFT")

start = st.date_input("Enter start date", datetime.date(2023, 7, 6))
end = st.date_input("Enter end date", datetime.date(2024, 7, 6))

ticker_df=ticker_data.history(period="1mo",start=start,end=end)

st.write("Here is the raw data:")
st.dataframe(ticker_df.head())

st.subheader("Line chart: price movement over time")
st.line_chart(ticker_df['Close'])



