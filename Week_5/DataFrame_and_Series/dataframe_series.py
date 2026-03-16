import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.to_string())


# my_dataset = {
#     "cars": ["BMW", "FORD", "CHEVROLET", "VOLVO"],
#     "passings": [3, 7, 5, 2]
# }
#
# my_var = pd.DataFrame(my_dataset)
# print(my_var)
# print(pd.__version__)

# a = [1, 2, 9, 5]
# series = pd.Series(a)
# print(series)
# print(series[2])
#
# own_indexes = pd.Series(a, index=['x', 'y', 'z', 'k'])
# print(own_indexes)
# print("Element by my own index:",own_indexes['x'])
#
# cars = {"Volvo": 1988, "Chevrolet": 2020, "Tesla": 2018}
# myvar = pd.Series(cars)
# print(myvar)
# print()
# my_var = pd.Series(cars, index=["Tesla", "Chevrolet"])
# print(my_var)

df = pd.DataFrame({
    "Name": ["Roy", "Alice", "Kaisa", "Dave"],
    "Age": [22, 53, 23, 19],
    "Sex": ["Male", "Female", "Female", "Male"]
})

# print(df)
# print(f"\nSeries with only names:\n{df['Name']}")
#
# print(f"\nSeries with only ages: \n{df['Age']}")

#Create Series from scratch
# job = pd.Series(['Python-Developer'], name='Job')
# print('\nCreate Series from scratch:\n', job)


#Find the maximum age of all passengers
# print(df["Age"].max())

#Iterate through entirely dataframe
# for i in df.items():
#     print("\nResult:\n", i)

#Iterate through series age with condition
# oldest = 0
# for j in pd.Series.items(df["Age"]):
#     if j[1] > oldest:
#         oldest = j[1]
#
# print(f"Oldest passenger in table has {oldest} years old.")

#Selecting a single column