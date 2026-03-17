import pandas as pd
#dropna
df = pd.read_csv("../Mall_Customers.csv")
dropna = df.dropna()
print(dropna.to_string())

dropna = df.dropna(how="all", subset=["Age", "CustomerID"])
print(dropna)
print()

#fillna - Replace empty values
fillna = df.fillna(92, inplace=True)
print(fillna)
print()

fillna_for_column = df.fillna({"Age": 30}, inplace=True)
print(fillna_for_column)
print()

#interpolate
interpolate = df.interpolate(method="linear") #by default
print(df.to_string())
print()

fill = df.bfill()
print(df.to_string())
print()

bfill = df.ffill()
print(df.to_string())
print()

interpolate_polynomial = df.interpolate(method="polynomial", order=2)
print(df.to_string())
print()

# interpolate_time = df.interpolate(method="time")    #Works only on Series or DataFrames with a DatetimeIndex
# print(interpolate_time)