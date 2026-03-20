import pandas as pd
import numpy as np

# df = {
#     "Name": ["Alice", "Alice", "Alice", "Jane", "Jane", "Jane", "Tom", "Tom", "Tom"],
#     "Subject": ["English", "French", "Spanish", "English", "French", "Spanish", "English", "French", "Spanish"],
#     "Points": [89, 75, 64, 78, 44, 87, 96, 83, 35],
#     "Result": ["Passed", "Passed", "Passed", "Passed", "Failed", "Passed", "Passed", "Passed", "Failed"]
# }
#
# df = pd.DataFrame(data=df)
# print(f"Without pivot:\n{df}")
# print(f"\nWith pivot:\n{df.pivot(index='Name',
#                                  columns='Subject',
#                                  values='Points')}")

# df = pd.DataFrame(data=df)
# df_2 = pd.DataFrame(data=df)
#
# print(df, '\n')
# print(df.pivot_table(index='Result', columns='Subject', values='Name', aggfunc='count', fill_value=0))
# df = pd.concat([df, pd.DataFrame({
#     "Name": ['Tom'],
#     "Subject": ['Spanish'],
#     "Points": [50],
#     "Result": ['Passed']
# })], ignore_index=True)

# print(df.pivot_table(index='Subject', columns='Name', values='Points'))
# print(f"\nRotate without aggregation (mean by default) makes int values:"
#       f"\n{df_2.pivot(index='Subject', columns='Name', values='Points')}")

#with margins (new columns ALL, partial group results) and round (rounding to hundredths)
# print(df.pivot_table(index='Subject', columns='Name', values='Points', margins=True, margins_name='mean').round(2))

#dropna=False and sort=False

# df_3 = pd.concat([df, pd.DataFrame({
#     "Name": ["Alex", "Alex", "Alex", "Alex"],
#     "Subject": ["English", "French", "Spanish", "German"],
#     "Points": [np.nan, np.nan, np.nan, 60],
#     "Result": ["Failed", "Failed", "Failed", "Passed"]
# })], ignore_index=True)
#
# print(df_3.pivot_table(
#     index='Subject',
#     columns='Name',
#     values='Points',
#     margins=True,
#     margins_name='mean',
#     dropna=False,
#     sort=False
# ).round(2))


# df = pd.DataFrame({
#     "User": ["Alice", "Alice", "Bob", "Bob", "Charlie", "Charlie", "Charlie", "Alice"],
#     "Product": ["Book", "Pen", "Book", "Pen", "Book", "Pen", "Pencil", "Book"],
#     "Category": ["Education", "Education", "Education", "Education", "Education", "Education", "Stationery", "Education"],
#     "Price": [10, 2, 12, 3, 15, 2, 1, 10],
#     "Quantity": [1, 3, 2, 5, 1, 2, 10, 2]
# })
#
# df_pivot = pd.DataFrame(data=df)
# print(f"Without pivot:\n{df_pivot}\n")

#
# try:
#     print(f"\nWith pivot:\n{df_pivot.pivot(index='User',
#                                        columns='Product',
#                                        values='Quantity')}")
# except Exception:
#     raise KeyError("DataFrame contains duplicate")

# df_pivot_table = pd.DataFrame(data=df)
# print(df_pivot_table.pivot_table(index='User',
#                            columns='Product',
#                            values='Quantity',
#                            aggfunc='sum'))


# df_mean = pd.DataFrame(data=df)
# print(df_mean.pivot_table(index=['User', 'Category', 'Price'],
#                           columns=['Product'],
#                           values='Quantity',
#                           aggfunc='mean',
#                           fill_value=0))


#---------- crosstable
# chocolate = {
#     "Brand": ["AlpenGold", "Nestle", "Milka"],
#     "Subject": [["Peanut", "Hazelnut", "Hazelnut", "Milk Chocolate"],
#                 ["Hazelnut", "Hazelnut", "Milk Chocolate", "Dark Chocolate"],
#                 ["Hazelnut", "Hazelnut", "Whole Hazelnut", "Milk Chocolate"]
#                 ],
#     "Weight_g": [[90, 90, 90, 90], [80, 80, 80, 80], [100, 100, 100, 100]],
#     "Price_(usd)": [[2.5, 2.5, 2.6, 2.0], [2.6, 2.6, 2.4, 2.8], [3.0, 3.0, 3.2, 2.9]]
# }
#
# df = pd.DataFrame(data=chocolate)
# exploded = df.explode(["Subject", "Weight_g", "Price_(usd)"]) #df.explode() - необходим для того, чтобы развернуть все данные в таблице со списков, массивов, и т.д., поскольку они свёрнуты в итерируемых объектах при большом размере mxn или nxn
# print(pd.crosstab([exploded['Brand'], exploded['Subject']], exploded['Weight_g']))

#print(pd.crosstab(index=[df["Brand"], df["Subject"]], columns=df["Weight_g"], values=df["Price_(usd)"]))


df = pd.read_csv('../car_sales_data.csv')
df = pd.DataFrame(data=df)
print(df.head(20).to_string(), '\n')
new_df = pd.crosstab(index=[["Manufacturer"], ["Year of manufacture"]], columns=df["Model"])
print(new_df.to_string())