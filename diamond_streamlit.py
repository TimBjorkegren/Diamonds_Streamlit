import streamlit as st
import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt

data_diamonds = pd.read_csv('diamonds.csv', sep=';')
data_diamonds = data_diamonds.dropna()
data_diamonds = data_diamonds.drop(columns=['Unnamed: 0'])
data_diamonds = data_diamonds.query('x > 0 and y > 0 and z > 0')

st.sidebar.title('Sidebar Menu')

page = st.sidebar.selectbox('Välj sida', [
    'Start',
    'Dataöversikt',
    'Filtrera diamanter',
    'Analys diamanter',
    'Slutsatser'
])

if page == 'Start':
    st.title('Välkommen till en Diamantanalys')
    st.write('Få en överblick över vår dataanalys över ett dataset av diamanter för att veta vilka som är mest prisvärda för ditt företag. '
             ' Vi har analyserat över 50 000 diamanter av olika kombinationer till olika värden. På sidebar menu så har vi olika kategorier som går djupare in i vår analys.')
    st.image('https://schalins.com/cdn/shop/articles/diamanter_c5f1f061-9124-432c-baa0-07f69d05e164_1400x.png?v=1741159661', use_container_width=True)

elif page == 'Dataöversikt':
    st.header('Dataöversikt')
    st.write(f'Dataframe med {data_diamonds.shape[0]} rader och {data_diamonds.shape[1]} kolumner')
    
    st.dataframe(data_diamonds)
    st.write('Statistik allmänt:')
    st.write(data_diamonds.describe())

elif page == 'Filtrera diamanter':
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

elif page == 'Analys diamanter':
    st.header('Analys diamanter')

elif page == 'Slutsatser':
    st.header('Slutsatser')    
