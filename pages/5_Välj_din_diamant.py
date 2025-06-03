import streamlit as st
import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

@st.cache_data()
def load_data():
    df = pd.read_csv('diamonds.csv', sep=';')

    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    df = df.dropna()
    df = df.query('x > 0 and y > 0 and z > 0')

    return df

data_diamonds = load_data()

#Poäng system
cut_scores = {'Ideal': 5, 'Premium': 4, 'Very Good': 3, 'Good': 2, 'Fair': 1}
color_scores = {'D':7 ,'E':6 ,'F':5 ,'G': 4,'H': 3, 'I': 2,'J': 1}
clarity_scores = {'IF': 8,'VVS1': 7,'VVS2': 6,'VS1': 5,'VS2': 4,'SI1': 3,'SI2': 2,'I1': 1}

st.header('Skapa din egen diamant och få en value score')

#Användarens input
carat = st.slider('Välj carat', min_value = 0.2, max_value = 5.0, step = 0.01, value = 1.0)
cut = st.selectbox('Välj cut', options = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Välj color', options = ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox('Välj clarity', options = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
price = st.number_input('Ange pris på diamant', min_value = 100, max_value = 20000, value = 5000)

#Poängberäkning
cut_score = cut_scores[cut]
color_score = color_scores[color]
clarity_score = clarity_scores[clarity]
quality_total_score = cut_score + color_score + clarity_score
price_per_carat = price / carat
value_score = quality_total_score / price_per_carat

#Visa användaren resultat
st.markdown(f'**Total Quality Score:** {quality_total_score}')
st.markdown(f'**Pris per carat:** {price_per_carat:.2f}')
st.markdown(f'### 💎 Value Score: {value_score:.5f}')

# Beräkna value score för hela dataframen
data_diamonds['price_per_carat'] = data_diamonds['price'] / data_diamonds['carat']
data_diamonds['cut_scores'] = data_diamonds['cut'].map(cut_scores)
data_diamonds['color_scores'] = data_diamonds['color'].map(color_scores)
data_diamonds['clarity_scores'] = data_diamonds['clarity'].map(clarity_scores)
data_diamonds['quality_total_score'] = data_diamonds['cut_scores'] + data_diamonds['color_scores'] + data_diamonds['clarity_scores']
data_diamonds['value_score'] = data_diamonds['quality_total_score'] / data_diamonds['price_per_carat']

#Räkna ut diamantens procent ranking
percentile_rank = (data_diamonds['value_score'] < value_score).mean() * 100
st.markdown(f'Din diamant är bättre än **{percentile_rank:.2f}%** av diamanterna i datasetet') 

fig, ax = plt.subplots(figsize = (8, 4))
ax.hist(data_diamonds['value_score'], bins = 50, color = 'skyblue')
ax.axvline(value_score, color = 'red', linestyle = 'dashed', linewidth = 2, label = 'Din diamant')
ax.set_title('Fördelning av value score')
ax.set_xlabel('Value score')
ax.set_ylabel('Antal diamanter')
ax.legend()
st.pyplot(fig)


if value_score > 0.005:
    st.success('Det här är en prisvärd diamant! ✅')
elif value_score > 0.003:
    st.info('Det här en okej diamant')
else:
    st.warning('Den här diamanten är inte prisvärd ❌')