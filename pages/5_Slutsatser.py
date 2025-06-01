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

st.header('Slutsats')
st.write('Syfte: Vår uppgift var att analysera ett dataset av diamanter för ett företag som skulle börja sälja diamanter, och våran uppgift var hur vi kunde hjälpa företaget med att analysera datasetet' \
'. Det som jag fastnade för var vilka typer av diamanter kan företaget köpa in för att få en så stor vinstmarginal på de typer av diamanter dom skulle köpa in. ' \
' Det jag har gjort är att jag har undersökt hur pris, karat, volym, color, clarity och cut påverkar priset och vilka enheter man ska använda för att ut mest pengar per karat i förhållande till kvaliteten ' \
' på diamanten, i detta fallet heter måttet value score.')

st.header('Viktigaste insikterna')
st.write('Det finns ett starkt samband mellan diamanternas value score och dess pris per karat, detta menas med att en diamants value score går upp i poäng om dess pris per karat är billigare' \
' eftersom man betalar mer för mindre karat när man överstiger vart majoriteten av diamanternas karat ligger på, i diagrammen så visar det sig att det kan vara en ökning på 8x om man vill ha 3x mer ' \
' karat på en diamant.' \
' ' \
' Vi har dessutom sett att vissa kombinationer av egenskaper gav bättre value score än andra eftersom våran metod består av att poängsätta egenskaper i en diamant som blir till en poäng summa' \
' som vi kan använda för att jämföra med andra diamanter.' \
' Mått som x, y, z alltså längd, bredd & djup i mm har ett negativt samband med value score alltså större diamanter var inte alltid mest prisvärda, dock det finns samband med att desto större' \
' en diamant är ju dyrare blir den vilket är logiskt korrekt.')

st.header('Value score')
st.write('Varför använder vi av måttet value score: Value score ger en möjlighet att jämföra prisvärdheten mellan diamanter med olika egenskaper där ett högre värde indikerar mer kvalitet per krona')

st.header('Rekommendationer')
st.write('Mina rekommendationer till kunder är att kolla inte på priset bara vissa diamanter erbjuder bättre värde sett till kvalitet. Dessutom mindre eller medelstora diamanter kan vara ' \
'kan vara mer prisvärda än stora, dock så får man tänka på att ju större en diamant är av en som är hög kvalitet desto mer sällsynt är den vilket kan göra att priset kan ökas väldigt mycket per karat')

st.header('Framtida förbättringar')

st.markdown("""
Även om analysen ger värdefulla insikter om diamanters prisvärde, finns det några begränsningar:

- **Ingen maskininlärning:** Istället för att använda enkel division (value score) hade mer advancerad modellering såsom maskininlärning kunnat ge mer exakt uppskattning av vad som påverkar priset. 

- **Attribut poängsättning:** Alla egenskaper (cut, color, clarity) väger lika mycket i value score medans det finns en sannolikhet att vissa väger mer än andra när det kommer till vad som påverkar priset.

- **Bättre visualisering: Kunde tilläga fler interaktiva visualiseringar som kan ge användaren möjligheten att själv utforska hur olika faktorer påverkar priset.**

- **Analysera trender: Man kunde researcha vilka diamanter som är mest populär vid säsonger för att hitta dom mest populära och rikta sig in mot dom för att ge företaget ett bättre förslag på diamanter.**                                 
            """)