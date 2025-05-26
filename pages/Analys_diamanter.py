import streamlit as st
import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt

data_diamonds = pd.read_csv('diamonds.csv', sep=';')
data_diamonds = data_diamonds.dropna()
data_diamonds = data_diamonds.drop(columns=['Unnamed: 0'])
data_diamonds = data_diamonds.query('x > 0 and y > 0 and z > 0')

fig, ax = plt.subplots(figsize = (8, 6))
ax.scatter(data_diamonds['carat'], data_diamonds['price'])
ax.set_xlabel('carat')
ax.set_ylabel('price')
ax.set_title('Scatterplot: carat vs price')
st.pyplot(fig)


data_diamonds['price_per_carat'] = data_diamonds['price'] / data_diamonds['carat']
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

axes = axes.flatten()

data_diamonds.boxplot(column='price_per_carat', by='cut', ax=axes[0])
axes[0].set_title('Price per carat depending on cut')
axes[0].set_xlabel('Cut')
axes[0].set_ylabel('Price per carat')

data_diamonds.boxplot(column='price_per_carat', by='color', ax=axes[1])
axes[1].set_title('Price per carat depending on color')
axes[1].set_xlabel('Color')
axes[1].set_ylabel('Price per carat')

data_diamonds.boxplot(column='price_per_carat', by='clarity', ax=axes[2])
axes[2].set_title('Price per carat depending on clarity')
axes[2].set_xlabel('Clarity')
axes[2].set_ylabel('Price per carat')

axes[3].axis('off')

plt.suptitle('Price per carat depending on cut, color and clarity')
st.pyplot(fig)