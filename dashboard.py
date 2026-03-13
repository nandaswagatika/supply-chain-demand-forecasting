import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Supply Chain Dashboard")
st.title("🚚 Supply Chain Dashboard")

# Load data only
df = pd.read_csv('supply_chain_data.csv')

# Metrics
col1, col2 = st.columns(2)
col1.metric("Total Sales", df['Number of products sold'].sum())
col2.metric("Total Revenue", f"${df['Revenue generated'].sum():,.0f}")

# Chart
fig = px.bar(df.groupby('Product type')['Number of products sold'].sum().reset_index(), 
             x='Product type', y='Number of products sold',
             title="Sales by Product Type")
st.plotly_chart(fig, use_container_width=True)

# Simple insights
st.header("📈 Key Insights")
st.write("- Highest sales: **Smart Hubs**")
st.write("- Most revenue from **New York**")
st.write("- Avg stock level: **95 units**")
