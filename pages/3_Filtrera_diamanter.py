import streamlit as st
import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt

@st.cache_data()
def load_data():
    df = pd.read_csv('diamonds.csv', sep=';')

    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    df = df.dropna()
    df = df.query('x > 0 and y > 0 and z > 0')

    return df

data_diamonds = load_data()

st.header('Filtrera diamanter')

carat_min, carat_max = st.slider('Välj carat gräns', float(data_diamonds.carat.min()), float(data_diamonds.carat.max()), (0.1, 1.0)) 

price_min, price_max = st.slider('Välj pris gräns', int(data_diamonds.price.min()), int(data_diamonds.price.max()), (500, 2000))

cut_options = st.multiselect('Välj typ av slipning (cut)', data_diamonds.cut.unique(), default = data_diamonds.cut.unique())

color_options = st.multiselect('Välj färg', data_diamonds.color.unique(), default = data_diamonds.color.unique())

clarity_options = st.multiselect('Välj klarhet', data_diamonds.clarity.unique(), default = data_diamonds.clarity.unique())

filtered_data_diamonds = data_diamonds[
    (data_diamonds.carat >= carat_min) & (data_diamonds.carat <= carat_max) &
    (data_diamonds.price >= price_min) & (data_diamonds.price <= price_max) &
    (data_diamonds.cut.isin(cut_options)) &
    (data_diamonds.color.isin(color_options)) &
    (data_diamonds.clarity.isin(clarity_options))
    ]

st.write(f'Antal diamanter som matchar ditt filter: {filtered_data_diamonds.shape[0]}')

st.dataframe(filtered_data_diamonds)