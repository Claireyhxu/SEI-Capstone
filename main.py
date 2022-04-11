# import statements
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime
import time
from datetime import date
from io import StringIO

# adding title and text in the app

# Links https://towardsdatascience.com/turn-excel-into-a-beautiful-web-application-using-streamlit-7a18516ca01a

st.write("Welcome to your first streamli application")
st.sidebar.title("Share Price analysis for May 2019 to May 2020:")
st.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.title("Gainers")
select = st.sidebar.selectbox('Share', ['Adani Green Energy', 'GMM Pfaudler', 'AGC Networks', 'Alkyl Amines Chem', 'IOL Chem & Pharma'], key='1')

# Adding our data
df = pd.read_excel("map.xlsx")


st.dataframe(df)


identities = df['Identity ']
# .drop_duplicates()
identity_choice = st.sidebar.selectbox('Select your identity:', identities)
# device = df["Device"].loc[df["Identity "] == identity_choice]
# year_choice = st.sidebar.selectbox('', device) 
