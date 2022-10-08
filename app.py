import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Sales Dashboard", 
                page_icon=":bar_chart:",
                layout="wide")

df = pd.read_excel(
    io='supermarkt_sales.xlsx',
    engine='openpyxl',
    sheet_name='Sales',
    skiprows=3,
    usecols='B:R',
    nrows=1000,
)


st.dataframe(df)

st.sidebar.header("Os filtros estão aqui:")

city = st.sidebar.multiselect(
    "Selecione a Cidade:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Selecione o tipo de cliente:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

gender = st.sidebar.multiselect(
    "Selecione o sexo:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)