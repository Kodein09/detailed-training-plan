import pandas as pd
import numpy as np

#---------- astype
df = pd.DataFrame(({"Name": ["Roy"], "Age": [20], "Height": [183]}))
astype = df.astype({"Age": "float", "Height": "bool"})
print("df dtypes:", df.dtypes)
print("", pd.DataFrame(data=astype).dtypes)

#---------- to_numeric
# df["Genre_num"] = df["Genre"].map({"Male": 0, "Female": 1})
# to_num = pd.to_numeric(df["Genre_num"], errors="coerce")
# print(to_num)

#---------- to_datetime
# df = pd.DataFrame({"Birth": ["1990-05-21", "2001-04-06", "2004/09/29"]})
# df["Birth_date"] = pd.to_datetime(df["Birth"], format="mixed", errors="coerce")
# print(df)