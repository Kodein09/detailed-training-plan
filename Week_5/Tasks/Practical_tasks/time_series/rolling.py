import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     "date": ["2000-01-01", "2000-01-02", "2000-01-03", "2000-01-04", "2000-01-05"],
#     "price": [39.81, 36.54, 40.35, 26.60, 28.37]
# })
#
# #lag (previous value)
# df["price_lag"] = df["price"].shift() #Можно сравнивать текущее значение с предыдущим, н-р, для сравнения вчерашней цены с сегодняшней.
#
# #lead (next value)
# df["price_lead"] = df["price"].shift(-1)
#
# print(df.isna().sum(), '\n')

# s = pd.Series([1,2,3,4,5])
# print(s)
# print(s.rolling(3).sum()) #window + aggregation
# df1 = s.rolling(window=3, min_periods=2, center=False).sum()
# df2 = s.rolling(window=3, min_periods=2, center=True).sum()
#
# print(pd.concat([df1, df2]))


# df1 = pd.DataFrame({
#     "A": [num for num in range(10, 30, 2)]
# })
# df2 = df1.rolling(window=2).sum()
# print(df1.join(other=df2, how="left", lsuffix="_x", rsuffix="_y"))

# df = pd.DataFrame(data={
#     "Product": ["KitKat", "Snickers", "Bounty", "Twix", "Mars", "Bueno", "Roshen", "MilkiWay", "Nuts"],
#     "Price_(kzt)": [700, 400, 400, 400, 350, 550, 250, 200, 400]
# })

# df["Price_rolling"] = df["Price_(kzt)"].rolling(window=3, win_type="triang").sum()
# df["Price_rolling"] = df["Price_(kzt)"].rolling(window=3, win_type="hann").sum()
# print(df, '\n')


# df_time = pd.DataFrame(
#     data={"Column": [0, 1, 2, np.nan, 4]},
#     index = pd.DatetimeIndex(data=[
#         pd.Timestamp("2026/03/25 09:00:00"),
#         pd.Timestamp("2026/03/25 09:00:02"),
#         pd.Timestamp("2026/03/25 09:00:04"),
#         pd.Timestamp("2026/03/25 09:00:06"),
#         pd.Timestamp("2026/03/25 09:00:08"),
#     ])
# )

#[current_time-2s, current_time)
#[08:59:58, 09:00:00) = Nan
#[09:00:00, 09:00:02) = 0 (left <= x < right) -> (09:00:00 <= )
# print(df_time.rolling(window="2s", closed='left').sum())