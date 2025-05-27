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


st.header('Dataöversikt')
st.write(f'Dataframe med {data_diamonds.shape[0]} rader och {data_diamonds.shape[1]} kolumner')
    
st.dataframe(data_diamonds)
st.write('Statistik allmänt:')
st.write(data_diamonds.describe())