import pandas as pd

data=pd.read_csv("stock_data.csv")

print(data.head())
print(data.columns)
print(data.info())
print(data.shape)

print(f"the mean is: {data['Price'].mean()}")
print(f"the max is: {data['Price'].max()}")
print(f"the min is: {data['Price'].min()}")

start_price=data['Price'].iloc[0]
end_price=data["Price"].iloc[-1]
print(f"the starting price is: {start_price}")
print(f"the ending price is: {end_price}")
print(f"the return is: {(end_price - start_price)/start_price * 100:.2f}%")

print(f"the volume mean is: {data['Volume'].mean()}")
max_volume=data["Volume"].max()
print(f"the date with the maximum volume is: {data[data['Volume']==max_volume]}")