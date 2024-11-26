import streamlit as st
import pandas as pd


st.title("Car Price Prediction - Veeranna")

cars_df=pd.read_csv("./cars24-car-price1.csv")
st.subheader("Data Frame:")
st.dataframe(cars_df.head())

