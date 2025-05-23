import streamlit as st
import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt


st.sidebar.title('Sidebar Menu')

page = st.sidebar.selectbox('Välj sida', [
    'Start',
    'Dataöversikt',
    'Filtrera diamanter',
    'Visualisera diamanter',
    'Slutsatser'
])

if page == 'Start':
    st.title('Välkommen till en Diamantanalys')
    st.write('Få en överblick över vår dataanalys över ett dataset av diamanter för att veta vilka som är mest prisvärda för ditt företag. '
             ' Vi har analyserat över 50 000 diamanter av olika kombinationer till olika värden. På sidebar menu så har vi olika kategorier som går djupare in i vår analys.')
    st.image('https://schalins.com/cdn/shop/articles/diamanter_c5f1f061-9124-432c-baa0-07f69d05e164_1400x.png?v=1741159661', use_container_width=True)

elif page == 'Dataöversikt':
    st.header('Dataöversikt')

elif page == 'Filtrera diamanter':
    st.header('Filtrera diamanter')

elif page == 'Visualisera diamanter':
    st.header('Visualisera diamanter')

elif page == 'Slutsatser':
    st.header('Slutsatser')    
