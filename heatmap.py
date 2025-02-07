import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(3, 2, figsize=(15, 8))
average_RSRP4G = []
average_RSRP5G = []
coverage_4G = []
coverage_5G = []

for index in range(3):
    filename = f'floor_{index}.csv'
    
    df = pd.read_csv(filename)
    df = df.iloc[:, [11, 29, 43, 44]]
    df = df.dropna()
    
    long = pd.to_numeric(df.iloc[:, 3])
    lat = pd.to_numeric(df.iloc[:, 2])
    RSRP5G = pd.to_numeric(df.iloc[:, 0])
    RSRP4G = pd.to_numeric(df.iloc[:, 1])
    
    #4G
    ax = axs[index, 0]
    scatter_4G = ax.scatter(long, lat, c=RSRP4G, cmap='jet')
    fig.colorbar(scatter_4G, ax=ax)
    ax.set_title(f'4G RSRP Signal Strength - Floor {index}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.grid(True)
    
    #5G
    ax = axs[index, 1]
    scatter_5G = ax.scatter(long, lat, c=RSRP5G, cmap='jet', s=60)
    fig.colorbar(scatter_5G, ax=ax)
    ax.set_title(f'5G RSRP Signal Strength - Floor {index}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.grid(True)

    avg_RSRP4G = RSRP4G.mean()
    avg_RSRP5G = RSRP5G.mean()
    average_RSRP4G.append(avg_RSRP4G)
    average_RSRP5G.append(avg_RSRP5G)

    # Analyze coverage (percentage of points above a certain threshold)
    threshold_4G = -90  # Good signal strength threshold for 4G (example: -90 dBm)
    threshold_5G = -85  # Good signal strength threshold for 5G (example: -85 dBm)
    
    # Calculate coverage as the percentage of points above the threshold
    coverage_4G_floor = (RSRP4G > threshold_4G).mean() * 100
    coverage_5G_floor = (RSRP5G > threshold_5G).mean() * 100
    
    coverage_4G.append(coverage_4G_floor)
    coverage_5G.append(coverage_5G_floor)
    
    #average signal strengths and coverage for each floor
    print(f"Floor {index} - Average 4G RSRP: {avg_RSRP4G:.2f} dBm")
    print(f"Floor {index} - Average 5G RSRP: {avg_RSRP5G:.2f} dBm")
    print(f"Floor {index} - 4G Coverage: {coverage_4G_floor:.2f}%")
    print(f"Floor {index} - 5G Coverage: {coverage_5G_floor:.2f}%\n")

#overall average signal strength across all floors
avg_RSRP4G_all = np.mean(average_RSRP4G)
avg_RSRP5G_all = np.mean(average_RSRP5G)

#overall coverage for all floors
coverage_4G_all = np.mean(coverage_4G)
coverage_5G_all = np.mean(coverage_5G)

#overall averages and coverage
print(f"Overall - Average 4G RSRP: {avg_RSRP4G_all:.2f} dBm")
print(f"Overall - Average 5G RSRP: {avg_RSRP5G_all:.2f} dBm")
print(f"Overall - 4G Coverage: {coverage_4G_all:.2f}%")
print(f"Overall - 5G Coverage: {coverage_5G_all:.2f}%")


plt.tight_layout(pad=2.0)
plt.show()

