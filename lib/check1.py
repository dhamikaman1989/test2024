import pandas as pd
import numpy as np

# Sample DataFrame
data = {'transaction_id': [1, 2, 3, 4, 5],
        'product_id': [101, 102, 103, 104, 105],
        'store_id': [1, 2, 1, 3, 2],
        'quantity': [2, 1, 5, 2, 3],
        'price': [10, 20, 15, 25, 30]}
df = pd.DataFrame(data)

print("dataframe we have is: ")
print(df)

# calc. total sales:
df["total_sales"] = df["quantity"] *df["price"]

# group by each store:
store_sales = df.groupby(["store_id","product_id"])["total_sales"].sum().reset_index()

print(store_sales)

print(store_sales.nlargest(2,"total_sales"))


# Sample DataFrame with missing values
data = {'numeric_col': [1, 2, np.nan, 4, 5],
        'category_col': ['A', 'B', np.nan, 'A', 'C']}
df = pd.DataFrame(data)

print("sample dataframe is: ")

print(df)

df["numeric_col"] = df["numeric_col"].fillna(df["numeric_col"].mean())

print(df)


