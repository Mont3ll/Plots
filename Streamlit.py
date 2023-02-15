import streamlit as st
import pandas as pd
import plotly.express as px

def data_header(dataframe):
    st.header('Data Header')
    st.write(data_2007_selection.head())

def scatter_plot(dataframe):
    x_axis=st.selectbox('Select x-axis value', options=data_2007.columns)
    y_axis=st.selectbox('Select y-axis value', options=data_2007.columns)
    col=st.color_picker('Select a plot colour')

    plot=px.scatter(data_2007_selection, x=x_axis, y=y_axis)
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

def violin_plot(dataframe):
    x_axis=st.selectbox('Select x-axis value', options=data_2007.columns)
    y_axis=st.selectbox('Select y-axis value', options=data_2007.columns)
    col=st.color_picker('Select a plot colour')

    plot=px.violin(data_2007_selection, x=x_axis, y=y_axis)
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

st.set_page_config(page_title="Data 2007",
                   page_icon=":bar_chart:",
                   layout="wide")

st.title("Data 2007")
st.text('GDP, Life Expectancy and Populaton for various countries for the year 2007.')

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
options=st.sidebar.radio(
         "Pages",
         options=['Home',
         'Data header',
         'Scatter plot',
         'Violin plot']
)
if options=='Home':
    st.dataframe(data_2007_selection)
elif options=='Data header':
    data_header(data_2007)
elif options=='Scatter plot':
    scatter_plot(data_2007)
elif options=='Violin plot':
    violin_plot(data_2007)
