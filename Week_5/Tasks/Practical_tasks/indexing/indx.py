import pandas as pd

print(pd.options.display.max_rows)

df = pd.read_csv("../train.csv")
df.dropna()
print(df.head().to_string(), '\n')

# loc = df.loc[198, "Genre"]
# iloc = df.iloc[199]
# query = df.query("Age > 68")
# print("loc:\n", loc)
# print()
# print("iloc:\n", iloc)
# print()
# print("query:\n", query)

# loc = df.loc[3]['Age'] #По индексу и столбце "Age"
# print(loc)
# print(df.loc[0])    #Returns a pandas Series
# print(df.loc[[0, 10]], '\n')    #Return row 0 and 10
#
# iloc = df.iloc[19]    #По индексу всю информацию из колонки 195
# print(iloc, '\n')
#
# query = df.query("Age > 69")
# print(query, '\n')
#
# conditional = df[df["Age"] < 20]
# print(conditional, '\n')
#
# conditional_filter = df[df["CustomerID"] == 1]
# print(conditional_filter, '\n')
#
# head = df.head(10)    #From 0-9 rows in tables
# print(head)
# print()
#
# print(df.info())
