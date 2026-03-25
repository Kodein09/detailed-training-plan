import pandas as pd

df = pd.DataFrame(data={
    "product": ["KitKat", "Snickers", "Bounty", "Twix", "Mars", "Bueno", "Roshen", "MilkiWay", "Nuts"],
    "price_(kzt)": [700, 400, 400, 400, 350, 550, 250, 200, 400],
    "weight_g": [50, 85, 80, 90, 45, 45, 30, 35, 50]
})

# print(df.expanding(min_periods=1).sum(numeric_only=True))
# print(df["price_(kzt)"].cumsum())
#Returns value - pandas.api.typing.Expanding