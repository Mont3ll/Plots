import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data 2007",
                   page_icon=":bar_chart:",
                   layout="wide")

data=pd.read_csv("gapminder_with_codes.csv")
data_2007=data[data['year']==2007]

st.sidebar.header("Filter:")
continent=st.sidebar.multiselect(
         "Select the continent:",
         options=data_2007["continent"].unique(),
         default=data_2007["continent"].unique()
)
data_2007_selection=data_2007.query(
         "continent==@continent"
)
st.dataframe(data_2007_selection)
