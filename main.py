import pandas as pd

data=pd.read_csv("stock_data.csv")

print(data.head())
print(data.columns)
print(data.info())
print(data.shape)

print(data.mean())
print(data.max())
print(data.min())