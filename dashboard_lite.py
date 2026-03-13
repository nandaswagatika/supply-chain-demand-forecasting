import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Supply Chain Dashboard")
st.title("🚚 Supply Chain Dashboard")

df = pd.read_csv('supply_chain_data.csv')

col1, col2 = st.columns
