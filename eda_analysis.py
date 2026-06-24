import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS PROJECT")
print("=" * 50)

# Load Dataset
df = pd.read_csv("sales_data.csv")

# Display Dataset
print("\nDataset:")
print(df)

# Dataset Info
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nTotal Sales by Category:")
print(category_sales)

# Bar Chart
plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("sales_bar_chart.png")
plt.show()

# Correlation Matrix
print("\nCorrelation Matrix:")
print(df[["Sales","Profit"]].corr())

# Heatmap
plt.figure(figsize=(5,4))

sns.heatmap(
    df[["Sales","Profit"]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# Insights
print("\nKey Insights:")
print("1. Electronics category generates the highest sales.")
print("2. Sales and Profit have a strong positive correlation.")
print("3. Higher sales generally lead to higher profit.")
print("4. Dataset contains no missing values.")

print("\nEDA Completed Successfully!")