import streamlit as st
import pandas as pd 
import numpy as np
import requests
import matplotlib.pyplot as plt

# Setting up the dataframe and cleaning it up
data_diamonds = pd.read_csv('diamonds.csv', sep=';')
data_diamonds = data_diamonds.dropna()
data_diamonds = data_diamonds.drop(columns=['Unnamed: 0'])
data_diamonds = data_diamonds.query('x > 0 and y > 0 and z > 0')

# Counting the price per carat
data_diamonds['price_per_carat'] = data_diamonds['price'] / data_diamonds['carat']

#Higher number equals higher quality based on the type of category
cut_scores = {'Ideal': 5, 'Premium': 4, 'Very Good': 3, 'Good': 2, 'Fair': 1}
color_scores = {'D':7 ,'E':6 ,'F':5 ,'G': 4,'H': 3, 'I': 2,'J': 1}
clarity_scores = {'IF': 8,'VVS1': 7,'VVS2': 6,'VS1': 5,'VS2': 4,'SI1': 3,'SI2': 2,'I1': 1}

#Making new columns with scores based on the quality
data_diamonds['cut_scores'] = data_diamonds['cut'].map(cut_scores)
data_diamonds['color_scores'] = data_diamonds['color'].map(color_scores)
data_diamonds['clarity_scores'] = data_diamonds['clarity'].map(clarity_scores)

#Adding the scores together per diamond
data_diamonds['quality_total_score'] = data_diamonds['cut_scores'] + data_diamonds['color_scores'] + data_diamonds['clarity_scores']

#Grouping all diamonds that have the same qualities into groupes and then taking the median value
data_diamonds['value_score'] = data_diamonds['quality_total_score'] / data_diamonds['price_per_carat']
median_value = data_diamonds.groupby(['cut', 'color', 'clarity', 'quality_total_score'])['value_score'].median().reset_index()
top_value = median_value.sort_values(by='value_score', ascending=False).head(10)



# Heatmap for correlations between different qualities 
cols = ["carat", "x", "y", "z", "price", "price_per_carat", "value_score"]
corr = data_diamonds[cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
fig.colorbar(cax)
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha='left')
ax.set_yticklabels(corr.columns)
st.pyplot(fig)


# Scatter plot for carat vs price
fig, ax = plt.subplots(figsize = (8, 6))
ax.scatter(data_diamonds['carat'], data_diamonds['price'])
ax.set_xlabel('carat')
ax.set_ylabel('price')
ax.set_title('Scatterplot: carat vs price')
st.pyplot(fig)

# Boxplots graphs for price per carat depending on cut, clarity and color
st.header('Boxplot graph: Pris per karat på cut, clarity & color')
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


# Scatterplot for quality score

col1, col2 = st.columns([4, 2])

with col1:
    st.header('Pris per karat baserat på kvalitets poäng')
    fig, ax = plt.subplots(figsize = (8, 5))
    ax.scatter(data_diamonds['quality_total_score'], data_diamonds['price_per_carat'])
    ax.set_title('Price per carat based on quality score')
    ax.set_xlabel('Quality score (color, clarity, cut)')
    ax.set_ylabel('price per carat')
    ax.grid(True)
    st.pyplot(fig)
    st.write('Deras poäng adderas ihop då till en summa som blir quality total score för att ha ett poäng system.')
    st.write('Quality total score kommer sedan bli divideras med "pris per karat" för att bli ett gemensamt värde: "Value Score"')

with col2:
    st.markdown("### Score Information:")
    st.markdown("""
    **Cut scores:**  
    - Ideal: 5  
    - Premium: 4  
    - Very Good: 3  
    - Good: 2  
    - Fair: 1  

    **Color scores:**  
    - D: 7  
    - E: 6  
    - F: 5  
    - G: 4  
    - H: 3  
    - I: 2  
    - J: 1  

    **Clarity scores:**  
    - IF: 8  
    - VVS1: 7  
    - VVS2: 6  
    - VS1: 5  
    - VS2: 4  
    - SI1: 3  
    - SI2: 2  
    - I1: 1
    """)

# Displaying dataframe of diamonds only the 10 best
st.header('Bästa diamanter baserad på deras value score (Top 10)')
st.dataframe(top_value.style.background_gradient(cmap='YlGn'))