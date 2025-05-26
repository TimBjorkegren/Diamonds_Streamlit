import streamlit as st
import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt

#source venv/Scripts/activate


data_diamonds = pd.read_csv('diamonds.csv', sep=';')
data_diamonds = data_diamonds.dropna()
data_diamonds = data_diamonds.drop(columns=['Unnamed: 0'])
data_diamonds = data_diamonds.query('x > 0 and y > 0 and z > 0')


st.title('Välkommen till en Diamantanalys')
st.write('Få en överblick över vår dataanalys över ett dataset av diamanter för att veta vilka som är mest prisvärda för ditt företag. '
             ' Vi har analyserat över 50 000 diamanter av olika kombinationer till olika värden. På sidebar menu så har vi olika kategorier som går djupare in i vår analys.')
st.image('https://schalins.com/cdn/shop/articles/diamanter_c5f1f061-9124-432c-baa0-07f69d05e164_1400x.png?v=1741159661', use_container_width=True)