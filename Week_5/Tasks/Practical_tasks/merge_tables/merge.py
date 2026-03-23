import pandas as pd
import numpy as np

# dataset = {
#     "Brand": ["AlpenGold", "Nestle", "Milka"],
#     "Subject": [["Peanut", "Hazelnut", "Hazelnut", "Milk Chocolate"],
#                 ["Hazelnut", "Hazelnut", "Milk Chocolate", "Dark Chocolate"],
#                 ["Hazelnut", "Hazelnut", "Whole Hazelnut", "Milk Chocolate"]
#                 ],
#     "Weight_g": [[90, 90, 90, 90], [80, 80, 80, 80], [100, 100, 100, 100]],
#     "Price_(usd)": [[2.5, 2.5, 2.6, 2.0], [2.6, 2.6, 2.4, 2.8], [3.0, 3.0, 3.2, 2.9]]
# }
#
# new_chocolate = {
#     "Brand": ["Mars", "Snickers", "Twix"],
#     "Subject": [["Chocolate 50%", "Chocolate 50%", "Milk Chocolate", "Milk Chocolate"],
#                 ["Caramel", "White Chocolate", "Milk Chocolate", "Dark Chocolate"],
#                 ["Dark Chocolate", "Milk Chocolate", "White Chocolate", "Ice Cream"]],
#     "Weight_g": [[50, 55, 45, 40],
#                  [45, 40, 55, 50],
#                  [95, 45, 50, 55]],
#     "Price_(usd)": [[2.5, 2.5, 2.6, 2.0],
#                     [2.6, 2.6, 2.4, 2.8],
#                     [3.0, 3.0, 3.2, 2.9]]
# }
#
# new_df = pd.DataFrame(data=new_chocolate)
# new_df = new_df.explode(["Subject", "Weight_g", "Price_(usd)"])
#
# df = pd.DataFrame(data=dataset)
# df = df.explode(["Subject", "Weight_g", "Price_(usd)"])
# print(df, '\n')
#
# print(df.merge(right=new_df, on='Subject', how='left', suffixes=('_old', '_new')).to_string())

# df1 = pd.DataFrame({
#     'Name': ['Tom', 'Bob', 'Alice'],
#     'Age': [25, 30, 22]
# })
#
# df2 = pd.DataFrame({
#     'Name': ['Tom', 'Alice', 'John'],
#     'Salary': [1000, 1500, 2000]
# })
#
# print(df1.merge(df2, on='Name', how='left'))

# merged = df1.merge(df2, how="inner", on='Name')
# print(merged)


# df1 = pd.DataFrame({
#     'Product': ['A', 'A', 'B'],
#     'Price': [10, 12, 20]
# })
#
# df2 = pd.DataFrame({
#     'Product': ['A', 'A', 'B'],
#     'Stock': [100, 200, 300]
# })
#
# print(f"{df1}\n\n{df2}\n")
# print(df1.merge(df2, on='Product'))

# sales = pd.DataFrame({
#     'product_id': [1, 1, 2, 2, 3],
#     'date': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-03', '2024-01-01'],
#     'revenue': [100, 150, 200, 250, 300]
# })
#
# products = pd.DataFrame({
#     'product_id': [1, 1, 2, 3, 3],
#     'category': ['A', 'B', 'A', 'C', 'D']
# })
#
# print(sales.merge(right=products, on="product_id", how='left'))


# dogs = pd.DataFrame(data={
#     "owner": ["owner_1", "owner_2", "owner_3"],
#     "dog": ["dog_1", "dog_2", "dog_3"],
#     "nickname": ["orange", "bobik", "lucy"]
# })
#
# cats = pd.DataFrame(data={
#     "owner": ["owner_1", "owner_2", "owner_4"],
#     "cat": ["cat_1", "cat_2", "cat_4"],
#     "nickname": ["orange", "lucy", "lucy"]
# })
#
# print(dogs.merge(right=cats))
# print('\n', dogs.merge(right=cats, on='owner', how='left', suffixes=('_dog', '_cat')))


# df1 = pd.DataFrame({
#     "A": ["A1", "A2", "A3"],
#     "B": ["B1", "B2", "B3"],
#     "C": ["C1", "C2", "C3"]
# }, index=["One", "Two", "Three"])
#
# df2 = pd.DataFrame({"B": ["B4", "B5"], "C": ["C4", "C5"], "D": ["D4", "D5"]}, index=["Four", "Five"])

# print(f"{df1}\n\n{df2}")

# print(pd.concat([df1, df2]))

# print(pd.concat([df1, df2], axis=1, join='inner'))
# print(pd.concat([df1, df2], join='outer'))
# print(pd.concat([df1, df2], join='inner'))

# df3 = pd.DataFrame({
#     "A": ["A1", "A2", "A3"],
#     "B": ["B1", "B2", "B3"],
#     "C": ["C1", "C2", "C3"]
# }, index=["One", "Two", "Three"])
#
# df4 = pd.DataFrame({
#     "D": ["D1", "D3"],
#     "E": ["E1", "E3"]
# }, index=["One", "Three"])
#
# print(pd.concat([df3, df4], axis=1, join='inner'))


# emp = pd.DataFrame({
#     "employee_id": [1003, 1004, 1007, 1012, 1022],
#     "FNLN_employee": ["Ivanov A.A.", "Petrov E.H.", "Ivanov A.A.", "Kuznecov P.R.", "Kozlov K.B."]
# })
#
# projects = pd.DataFrame({
#     "employee_id": [1003, 1012, 1022, 2022, 3005],
#     "project_code": ["P_24", "P_17", "P_05", "P_13", "P_02"]
# })
#
# print(f"{emp}\n\n{projects}\n\n")

#merge inner
# print(emp.merge(right=projects, on="employee_id", how='inner'))

#merge left
# print(emp.merge(right=projects, on="employee_id", how='left'))

#merge right
# print(emp.merge(right=projects, on='employee_id', how='right'))

#merge outer все строки левой и правой таблицы без исключения войдут в результат слившись по ключу
# print(projects.merge(right=emp, on='employee_id', how='outer', indicator=True))

#merge cross создаются всевозможные комбинации левой и правой таблицы, в cross нельзя прописывать параметр on=''
# print(emp.merge(right=projects, how='cross', suffixes=('_x', '_y'), indicator='indicator'))

# print(emp.set_index(keys="employee_id").merge(right=projects, left_index=True, right_on='employee_id'))



#---------- join
# df = pd.DataFrame({
#     "key": ["K0", "K1", "K2", "K3", "K4"],
#     "A": ["A0", "A1", "A2", "A3", "A4"]
# })
# print(df, '\n')
#
other = pd.DataFrame({"key": ["K0", "K1", "K2"], "B": ["B0", "B1", "B2"]})
# print(other, '\n')

# print(df.join(other=other, lsuffix="_left", rsuffix="_right")) #Join dataframes using their indexes ([0, 1, 2, 3, 4, ...]).
# print(df.set_index("key").join(other=other.set_index("key"), lsuffix="_left", rsuffix="_right"))

# print(df.join(other=other.set_index(keys='key'), on='key'))


# df = pd.DataFrame(
#     {
#         "key": ["K0", "K1", "K1", "K3", "K0", "K1"],
#         "A": ["A0", "A1", "A2", "A3", "A4", "A5"],
#     }
# )
# print(df.join(other=other.set_index(keys='key'), on='key', validate='many_to_one'))