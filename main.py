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
print(f"the date with the maximum volume is {data[data['Volume']==max_volume]['Date'].iloc[0]} which has a volume of {max_volume}")

highest_price=data["Price"].max()
highest_price_date=data[data["Price"]==highest_price]["Date"].iloc[0]
print(f"the highest price is {highest_price} which occurred on {highest_price_date}")

lowest_price=data["Price"].min()
lowest_price_date=data[data["Price"]==lowest_price]["Date"].iloc[0]
print(f"the lowest price is {lowest_price} which occurred on {lowest_price_date}")

data["Daily_Returns"]=data["Price"].pct_change() * 100

print(data)

average_price_change=data["Daily_Returns"].mean()
max_price_change=data["Daily_Returns"].max()
min_price_change=data["Daily_Returns"].min()

print(average_price_change)
print(max_price_change)
print(min_price_change)

date_max_return=data[data["Daily_Returns"]==max_price_change]["Date"].iloc[0]
date_min_return=data[data["Daily_Returns"]==min_price_change]["Date"].iloc[0]

print(f"the highest return was {max_price_change} on {date_max_return}")
print(f"the lowest was {min_price_change} on {date_min_return}")

significant_returns=data[(data["Daily_Returns"] > 2) | (data["Daily_Returns"] < -2)]["Date"]
print(f"days where return was greater or less than 2%: {significant_returns}")

positive_days = data[data["Daily_Returns"] > 0]
print(f"the number of positive days is {positive_days.shape[0]}")

negative_days = data[data["Daily_Returns"] < 0]
print(f"the number of negative days is {negative_days.shape[0]}")

