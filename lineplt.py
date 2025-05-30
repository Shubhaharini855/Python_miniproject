import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
df = pd.read_csv(r"C:\Users\HP\Downloads\Train.csv")
print(df)
# Group and count shipments per Warehouse block
Volume_by_carrier = df.groupby('Warehouse_block')['Mode_of_Shipment'].count().reset_index()
Volume_by_carrier.rename(columns={'Mode_of_Shipment': 'Shipment_Count'}, inplace=True)

# Plot as line plot
plt.figure(figsize=(5, 6))
sns.lineplot(data=Volume_by_carrier, x='Warehouse_block', y='Shipment_Count', marker='o', color='green')
plt.title('Shipment Volume by Warehouse Block (Line Plot)')
plt.xlabel('Warehouse Block')
plt.ylabel('Number of Shipments')
plt.tight_layout()
plt.show()