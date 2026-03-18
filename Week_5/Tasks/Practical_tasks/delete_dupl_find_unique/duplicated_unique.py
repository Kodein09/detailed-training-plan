import pandas as pd
import numpy as np

# df = {
#     "Name": ["Alex", "Alex", "Solomon"],
#     "Age": [25, 25, 32],
#     "Car": ["Chevrolet", "Chevrolet", "Ford"]
# }
# df = pd.DataFrame(data=df)
# print(df, end='\n\n')
# dupl = df.duplicated()
# print(dupl)
# print(df[df.duplicated()])


# df= {
#     "Name": ["Dave", "Alice", "Bob", "Charlie", "Ellen"],
#     "Age": [26, 32, 48, 42, 22],
#     "State": ["NY", "TX", "LA", "CA", "NY"],
#     "Point": [65, 69, 83, 94,75]
# }
# df = pd.DataFrame(data=df)
# df.loc[5] = ["Husle", 38, "TX", 77]
# df.loc[6] = ["Joe", 52, "NY", 55]
# df.loc[7] = ["Bob", 48, "LA", 83]
# print(df, end='\n\n')
#
# df_keep = df.duplicated(keep='first') #By default
# print(f"keep first by default:\n{df_keep[df_keep.duplicated()]}")
# df_keep = df.duplicated(keep='last')
# print(f"keep last:\n{df_keep[df_keep.duplicated()]}")

# df_subset = df.duplicated(subset="Age")
# print(f"Duplicated:\n{df_subset}\n")
# print(f"Duplicated row is:\n{df[df.duplicated()]}")

# df = {
#     "Product": ["Milk chocolate 80%", "Milk chocolate 70%", "White chocolate 100%", "Chocolate 30%"],
#     "Brand": ["Oreo", "KitKat", "Milka", "Snickers"],
#     "Price_$": [2, 3, 4, 3],
#     "weight_g": [80, 50, 90, 50]
# }
# df_dd = pd.DataFrame(data=df)
# df_dd.loc[4] = ["Truffile 30%", "Ferrero Rocher", 8, 100]
# df_dd.loc[5] = ["Milk chocolate 80%", "Oreo", 2, 80]
# df_dd.loc[6] = ["Milk chocolate 70%", "KitKat", 3, 50]
# print(f"With duplicates:\n{df_dd}\n")
#
# df_dd = df_dd.drop_duplicates()
# print(f"And without duplicates:\n{df_dd}")

# df.ffill(inplace=True)    #Replace empty values by prev values
#df.duplicated()    #Find duplicates if only for check
#df = df.drop_duplicates(subset=["CustomerID"])    #Delete dupl and save first
# df = df[df.duplicated(keep=False) == False]    #Delete all dupl include first value
# print(df, end='\n\n')



#--------- Unique
# unique_for_series = pd.Series([10, 53, 25, 40, 32, 32, 10, 53])
# print(f"Without unique:\n{unique_for_series}")
# print(f"With unique:\n{unique_for_series.unique()}")

df_with_messing_values = {
    "Type of meat": [np.nan, "Beef", "Fish", "Mutton", "Pork"],
    "Weight_kg": [1.5, 0.900, np.nan, 1, 2],
    "Price_$": [5, 10, 12, 8, np.nan]
}

df = pd.DataFrame(data=df_with_messing_values)
print(df)

print(f"\nNunique with 'axis=0' (rows) and 'dropna=True' (don't include NaN in the counts):\n{df.nunique(axis=0, dropna=True)}") #Return series with counts of unique values per row or column, depending on axis. Can ignore NaN values.

print(f"\nNext print with 'axis=1' (cols) and 'dropna=False', where include NaN in the counts:\n{df.nunique(axis=1, dropna=False)}")
print(f"\nNext print with 'axis=1' (cols) and 'dropna=True', where include NaN in the counts:\n{df.nunique(axis=1, dropna=True)}")