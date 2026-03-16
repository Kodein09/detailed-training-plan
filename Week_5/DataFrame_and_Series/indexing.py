import pandas as pd

df = pd.read_csv('products.csv')
# print(df.head())
#
# survived = df["Survived"]
# print(f"Survived passenger in sequence from 0 to 4:\n{survived.head()}\nAnd his id:\n{df['PassengerId'].head()}")


multiply_column = df[["product_name", "brand", "category", "cocoa_percent", "weight_g"]]
print(multiply_column.head(), '\n')

print(f"Indexing with '.loc[n]', chocolate under index 4 with brand name is:\n{multiply_column.loc[4]['brand']}")

print(f"Indexing with '.iloc[n]', chocolate under index 4 with brand name is:\n{multiply_column.iloc[4]['brand']}")