import streamlit as st
import numpy as np
import matplotlib
import pandas as pd
import seaborn as sns

# Use non-interactive backend (safe for Streamlit deployment)
matplotlib.use('Agg')
from matplotlib.figure import Figure

st.title("Shipment Data Visualization")

# Load data
df = pd.read_csv("train.csv")

st.subheader("Raw Data")
st.dataframe(df)

# Group and count shipments per Warehouse block
Volume_by_carrier = df.groupby('Warehouse_block')['Mode_of_Shipment'].count().reset_index()
Volume_by_carrier.rename(columns={'Mode_of_Shipment': 'Shipment_Count'}, inplace=True)

# Bar Plot
st.subheader("Bar Plot: Shipment Volume by Warehouse Block")
fig1 = Figure(figsize=(5, 6))
ax1 = fig1.subplots()
sns.barplot(data=Volume_by_carrier, x='Warehouse_block', y='Shipment_Count', palette='Set3', ax=ax1)
ax1.set_title('Shipment Volume by Warehouse Block')
ax1.set_xlabel('Warehouse Block')
ax1.set_ylabel('Number of Shipments')
st.pyplot(fig1)

# Line Plot
st.subheader("Line Plot: Shipment Volume by Warehouse Block")
fig2 = Figure(figsize=(5, 6))
ax2 = fig2.subplots()
sns.lineplot(data=Volume_by_carrier, x='Warehouse_block', y='Shipment_Count', marker='o', color='green', ax=ax2)
ax2.set_title('Shipment Volume by Warehouse Block (Line Plot)')
ax2.set_xlabel('Warehouse Block')
ax2.set_ylabel('Number of Shipments')
st.pyplot(fig2)

# Heatmap
st.subheader("Heatmap: Shipment Mode Count per Warehouse Block")
heatmap_data = df.pivot_table(index='Warehouse_block', 
                               columns='Mode_of_Shipment', 
                               aggfunc='size', 
                               fill_value=0)

fig3 = Figure(figsize=(8, 6))
ax3 = fig3.subplots()
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.5, linecolor='gray', ax=ax3)
ax3.set_title('Heatmap: Shipment Mode Count per Warehouse Block')
st.pyplot(fig3)
