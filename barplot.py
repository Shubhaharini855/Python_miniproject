import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
df = pd.read_csv(r"C:\Users\HP\Downloads\Train.csv")

# Group and count shipments per Warehouse block
Volume_by_carrier = df.groupby('Warehouse_block')['Mode_of_Shipment'].count().reset_index()
Volume_by_carrier.rename(columns={'Mode_of_Shipment': 'Shipment_Count'}, inplace=True)

# Plot
plt.figure(figsize=(5, 6))
sns.barplot(data=Volume_by_carrier, x='Warehouse_block', y='Shipment_Count', palette='Set3')
plt.title('Shipment Volume by Warehouse Block')
plt.xlabel('Warehouse Block')
plt.ylabel('Number of Shipments')
plt.tight_layout()
plt.show()