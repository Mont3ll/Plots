import streamlit as st
import pandas as pd
import plotyl.express as px

st.set_page_config(page_title="Data 2007")

data=pd.read_csv("gapminder_with_codes.csv")
data_2007=data[data['year']==2007]
data_2007
