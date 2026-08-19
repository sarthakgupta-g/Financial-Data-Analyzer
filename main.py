import pandas as pd

data=pd.read_csv("stock_data.csv")

print(data.head())
print(data.columns)
print(data.info())
print(data.shape)

print(f"the mean is: {data['price'].mean()}")
print(f"the max is: {data['price'].max()}")
print(f"the min is: {data['price'].min()}")