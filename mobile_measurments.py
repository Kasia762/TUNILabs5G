import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df4G = pd.read_csv('test_data.csv')
df5G = pd.read_csv('test_data.csv')

def mean_values(data):
    DL_mean = round(data["DL"].mean())
    UL_mean = round(data["UL"].mean())
    latency_mean = round(data["latency"].mean())
    jitter_mean = round(data["jitter"].mean()) 
    return [DL_mean,UL_mean,latency_mean,jitter_mean]

df4G_mean = mean_values(df4G)
df5G_mean = mean_values(df5G)

mean_df = pd.DataFrame({
    'Metric': ['DL', 'UL', 'Latency', 'Jitter'],
    '4G': df4G_mean,
    '5G': df5G_mean
})

fig, ax = plt.subplots(figsize=(6, 2))
ax.axis('off')
table = ax.table(cellText=mean_df.values, 
                 colLabels=mean_df.columns, loc='center', 
                 cellLoc='center')
plt.savefig('mean_values_table.jpg', bbox_inches='tight', 
            dpi=300)
plt.show()