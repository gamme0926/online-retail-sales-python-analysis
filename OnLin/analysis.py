import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ==========================
# Load Data
# ==========================

print("Loading dataset...")

df=pd.read_csv( "onlineCSV.csv",
    encoding="latin1",
    low_memory=False
)

print("Dataset loaded successfully.\n")

# ==========================
# Basic Information
# ==========================

print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print(df.shape)

print("\n")

print("=" * 60)
print("DATASET INFO")
print("=" * 60)

print(df.info())

print("\n")

# ==========================
# Missing Values
# ==========================

print("=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

print("\n")

# ==========================
# Data Cleaning
# ==========================

# Remove rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove negative or zero UnitPrice
df = df[df["UnitPrice"] > 0]

# Create Revenue Column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("=" * 60)
print("DATA CLEANING COMPLETE")
print("=" * 60)

print("Remaining Rows:", len(df))

print("\n")

# ==========================
# Revenue Summary
# ==========================

print("=" * 60)
print("REVENUE SUMMARY")
print("=" * 60)

print(df["Revenue"].describe())

print("\n")

# ==========================
# Top 10 Countries By Revenue
# ==========================

top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 COUNTRIES BY REVENUE")
print("=" * 60)

print(top_countries)

print("\n")

# ==========================
# Top 10 Products By Revenue
# ==========================

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 PRODUCTS BY REVENUE")
print("=" * 60)

print(top_products)

print("\n")

# ==========================
# Top 10 Customers
# ==========================

top_customers = (
    df.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("=" * 60)
print("TOP 10 CUSTOMERS")
print("=" * 60)

print(top_customers)

print("\n")

# ==========================
# Create Charts Folder
# ==========================

Path("charts").mkdir(exist_ok=True)

# ==========================
# Chart 1
# Top Countries
# ==========================

plt.figure(figsize=(12,6))

top_countries.plot(
    kind="bar",
    color="steelblue"
)

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "charts/top_countries.png",
    bbox_inches="tight"
)

plt.close()

# ==========================
# Chart 2
# Top Products
# ==========================

plt.figure(figsize=(12,6))

top_products.plot(
    kind="bar",
    color="green"
)

plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig(
    "charts/top_products.png",
    bbox_inches="tight"
)

plt.close()

# ==========================
# Chart 3
# Revenue Distribution
# ==========================

plt.figure(figsize=(10,6))

sns.histplot(
    df["Revenue"],
    bins=30,
    kde=True
)

plt.title("Revenue Distribution")

plt.tight_layout()

plt.savefig(
    "charts/revenue_distribution.png",
    bbox_inches="tight"
)

plt.close()

# ==========================
# Chart 4
# Correlation Heatmap
# ==========================

corr = (
    df[
        ["Quantity", "UnitPrice", "Revenue"]
    ]
    .corr()
)

plt.figure(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "charts/correlation_heatmap.png",
    bbox_inches="tight"
)

plt.close()

# ==========================
# Business Insights
# ==========================

highest_country = top_countries.index[0]
highest_country_revenue = top_countries.iloc[0]

highest_product = top_products.index[0]
highest_product_revenue = top_products.iloc[0]

print("=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print(
    f"Top Country: {highest_country}"
)

print(
    f"Revenue: {highest_country_revenue:,.2f}"
)

print()

print(
    f"Top Product: {highest_product}"
)

print(
    f"Revenue: {highest_product_revenue:,.2f}"
)

print()

print(
    f"Total Revenue: {df['Revenue'].sum():,.2f}"
)

print("\nAnalysis Completed Successfully!")