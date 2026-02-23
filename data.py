import pandas as pd

# Creating sales data
data = {
    "Month": ["January", "January", "February", "February", "March", "March"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile", "Laptop", "Mobile"],
    "Quantity": [5, 10, 3, 8, 6, 12],
    "Price": [50000, 20000, 50000, 20000, 50000, 20000]
}

df = pd.DataFrame(data)

# Calculate total sales for each row
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("Sales Data:\n", df)

# Total overall sales
print("\nTotal Overall Sales:", df["Total_Sales"].sum())

# Best selling product
print("\nBest Selling Product:")
print(df.groupby("Product")["Total_Sales"].sum())

# Monthly sales
print("\nMonthly Sales:")
print(df.groupby("Month")["Total_Sales"].sum())

# Average monthly sales
print("\nAverage Monthly Sales:", df.groupby("Month")["Total_Sales"].sum().mean())
