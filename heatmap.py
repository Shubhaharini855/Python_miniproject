import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
df = pd.read_csv(r"C:\Users\HP\Downloads\Train.csv")

# Create a pivot table: counts of Mode_of_Shipment per Warehouse_block
heatmap_data = df.pivot_table(index='Warehouse_block', 
                               columns='Mode_of_Shipment', 
                               aggfunc='size', 
                               fill_value=0)

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', linewidths=0.5, linecolor='gray')
plt.title('Heatmap: Shipment Mode Count per Warehouse Block')
plt.xlabel('Mode of Shipment')
plt.ylabel('Warehouse Block')
plt.tight_layout()
plt.show()
