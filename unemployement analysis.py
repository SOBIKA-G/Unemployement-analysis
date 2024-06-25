import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load datasets
df1 = pd.read_csv("D:\\Python\\Unemployment in India.csv")
df2 = pd.read_csv("D:\\Python\\Unemployment_Rate_upto_11_2020.csv")

# Check and clean column names
print("Dataset 1 Columns:", df1.columns)
print("Dataset 2 Columns:", df2.columns)

# Strip any leading/trailing spaces from column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Strip leading/trailing spaces from date columns and convert to datetime
df1['Date'] = pd.to_datetime(df1['Date'].str.strip(), format='%d-%m-%Y')
df2['Date'] = pd.to_datetime(df2['Date'].str.strip(), format='%d-%m-%Y')

# Descriptive statistics
print(df1.describe())
print(df2.describe())

avg_unemployment_df1 = df1.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
avg_unemployment_df2 = df2.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

# Ensure both DataFrames have the same index (regions)
avg_unemployment_df1 = avg_unemployment_df1.reindex(avg_unemployment_df2.index)

# Plotting
plt.figure(figsize=(12, 8))

# Bar width
bar_width = 0.35

# Positions of bars on x-axis
r1 = np.arange(len(avg_unemployment_df1))
r2 = [x + bar_width for x in r1]

# Plot bars
plt.bar(r1, avg_unemployment_df1, color='blue', width=bar_width, edgecolor='grey', label='Pre-COVID-19')
plt.bar(r2, avg_unemployment_df2, color='red', width=bar_width, edgecolor='grey', label='During COVID-19')

# Add labels and title
plt.xlabel('Region')
plt.ylabel('Average Unemployment Rate (%)')
plt.title('Average Unemployment Rate Comparison (Pre-COVID-19 vs During COVID-19)')

# Add x-axis tick labels and rotate them vertically
plt.xticks([r + bar_width / 2 for r in range(len(avg_unemployment_df1))], avg_unemployment_df1.index, rotation=90)

# Add legend
plt.legend()

# Show plot
plt.tight_layout()
plt.show()