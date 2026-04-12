import pandas as pd
import numpy as np
#dropna

df = {
    "Name": ["Roy", "Leonardo", "Alice"],
    "Age": [23, np.nan, 26],
    "Car": ["Ferrari", np.nan, "Honda"],
    "Annual Income (usd)": [100_000, 230_00, 300_000]
}
df = pd.DataFrame(data=df)
print(df, '\n')
print(f"DataFrame:\n{df.drop(axis=0, index=1, columns='Name')}\n")

# #dropna axis=0 (row)
# df1 = df.dropna(axis=0, inplace=False)
# print(f"dropna ROW:\n{df1}\n")
#
# #dropna axis=1 (column)
# df2 = df.dropna(axis=1 ,inplace=False)
# print(f"dropna COLUMN:\n{df2}")

#df_all = df.dropna(axis="rows", how="all")
# df_any = df.dropna(axis="columns", how="any")
# print(df_any)

# df_subset = df.dropna(axis="rows", subset='Car:', inplace=False)
# print(df_subset)

#subset delete row with NaN
# df_subset = df.dropna(subset='Car:', inplace=False)
# print(df_subset)

# df = pd.read_csv("../train.csv")
# df.dropna()
# print(df.head(10))

# dropna = df.dropna(how="all", subset=["Age", "CustomerID"])
# print(dropna)


#---------- fillna
#fillna - Replaces NaN with an arbitrary value
# fillna = df.fillna({"Age:": 50, "Car:": "Chevrolet"}, inplace=False)
# print(f"Fillna:\n{fillna}")
#
# fillna_for_column = df.fillna({"Age": 30}, inplace=True)
# print(fillna_for_column)


#---------- interpolate
# df = {
#     "Class A": [50, np.nan, 68, 60],
#     "Class B": [80, 90, np.nan, 70]
# }
#
# df = pd.DataFrame(data=df)
# df.interpolate(method="linear", inplace=True) #by default
# print(df)

#
# bill = df.bfill()
# print(df.to_string())
#
# ffill = df.ffill()
# print(df.to_string())
#
# interpolate_polynomial = df.interpolate(method="polynomial", order=2)
# print(df.to_string())

# interpolate_time = df.interpolate(method="time")    #Works only on Series or DataFrames with a DatetimeIndex
# print(interpolate_time)