import streamlit as st
import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt

data_diamonds = pd.read_csv('diamonds.csv', sep=';')
data_diamonds = data_diamonds.dropna()
data_diamonds = data_diamonds.drop(columns=['Unnamed: 0'])
data_diamonds = data_diamonds.query('x > 0 and y > 0 and z > 0')


st.header('Dataöversikt')
st.write(f'Dataframe med {data_diamonds.shape[0]} rader och {data_diamonds.shape[1]} kolumner')
    
st.dataframe(data_diamonds)
st.write('Statistik allmänt:')
st.write(data_diamonds.describe())