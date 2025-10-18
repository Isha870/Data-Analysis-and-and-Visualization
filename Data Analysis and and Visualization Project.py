 # Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 250, 300, 280, 350, 400],
    "Profit": [50, 70, 90, 80, 100, 120]
})

# Display basic info
print("Data Info:")
print(data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Display first 5 rows
print("\nFirst 5 rows:")
print(data.head())

# --------- VISUALIZATIONS ---------

# Line plot of Sales over Months
plt.figure(figsize=(8,5))
plt.plot(data['Month'], data['Sales'], marker='o', color='blue')
plt.title('Sales over Months')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Bar plot of Profit over Months
plt.figure(figsize=(8,5))
sns.barplot(x='Month', y='Profit', data=data, palette='viridis')
plt.title('Profit per Month')
plt.show()

# Scatter plot of Sales vs Profit
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', data=data, color='red', s=100)
plt.title('Sales vs Profit')
plt.show()



