# import statements
from distutils.filelist import findall
from faulthandler import disable
from operator import index
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
from functools import reduce
# adding title and text in the app

# Links https://towardsdatascience.com/turn-excel-into-a-beautiful-web-application-using-streamlit-7a18516ca01a

# st.write("Welcome to your first streamli application")
# st.sidebar.title("Share Price analysis for May 2019 to May 2020:")
# st.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
# st.sidebar.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
# st.sidebar.title("Gainers")
# select = st.sidebar.selectbox('Share', ['Adani Green Energy', 'GMM Pfaudler', 'AGC Networks', 'Alkyl Amines Chem', 'IOL Chem & Pharma'], key='1')

# Adding our data
df = pd.read_excel("map.xlsx")
column_name_primary_f = 'Primary Function'
column_name_secondary_f = 'Secondary Function'
primary_functions = df[column_name_primary_f].drop_duplicates().values.tolist()
secondary_functions = df[column_name_secondary_f].drop_duplicates().values.tolist()


st.sidebar.write("Control Family")

control_family_names = ["Identity", "Device","Network/Environment", "Application Workload", "Data"]
controlFamiliesSelections  = [
    st.sidebar.checkbox(s, value=True) for s in control_family_names
]
controlFamiliesSelections = [1 if i else 0 for i in controlFamiliesSelections]
[id, dev, netenv, appwl, dt] = controlFamiliesSelections
# identities = df['Identity ']
# .drop_duplicates()
# identity_choice = st.sidebar.selectbox('Select your identity:', identities)
# device = df["Device"].loc[df["Identity "] == identity_choice]
# year_choice = st.sidebar.selectbox('', device) 
def controlFilter(df):
    indexes = [df[control_family_names[i]] == controlFamiliesSelections[i] if controlFamiliesSelections[i] else 
        df[control_family_names[i]] == df[control_family_names[i]] 
      # don't care about selection if not selected
    for i in range(len(controlFamiliesSelections))]
    return df.loc[ 
        reduce(lambda x, y : x & y, indexes)
     ]
st.sidebar.write("---------------") 

pf_enable= st.sidebar.checkbox("Filter by Primary Function", value=False)
if pf_enable:
    pf_select = st.sidebar.selectbox("Primary Function",  primary_functions )
sf_enable = st.sidebar.checkbox("Filter by Secondary Function", value=False)
if sf_enable:
    sf_select = st.sidebar.selectbox("Secondary Function",  secondary_functions)


def functionFilter (df): 
    retDf = df
    if pf_enable:
        retDf = retDf[retDf[column_name_primary_f] == pf_select]
    if sf_enable:
        retDf = retDf[retDf[column_name_secondary_f] == sf_select]
    return retDf



print(controlFamiliesSelections)
finalDF = functionFilter(controlFilter(df))
st.write("Total {} lines".format(len(finalDF)))
st.dataframe(finalDF, width=800, height=600)
# st.table(finalDF)

st.write("\n\n".join(finalDF["Control Text"].values.tolist()))