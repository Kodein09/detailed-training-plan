import pandas as pd

#df = pd.read_csv("")
# print(df)
#
# df["Genre_num"] = df["Genre"].map({"Male": 0, "Female": 1})
# to_num = pd.to_numeric(df["Genre_num"], errors="coerce")
# print(to_num)


#to_date
df = pd.DataFrame({"Birth": ["1990-05-21", "2001-04-06", "2004/09/29"]})
df["Birth_date"] = pd.to_datetime(df["Birth"], format="mixed", errors="coerce")
print(df)

#astype
df = pd.DataFrame(({"Name": ["Roy"], "Age": [20], "Height": [183]}))
astype = df.astype({"Age": "float", "Height": "bool"})
#astype = df.astype(str)
print(astype.dtypes)