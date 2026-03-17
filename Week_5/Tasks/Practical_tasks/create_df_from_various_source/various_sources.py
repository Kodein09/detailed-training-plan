import matplotlib.pyplot as plt
import pandas as pd
import json

#Create dataframe from csv-file
df_csv = pd.read_csv("/Users/roias/PycharmProjects/Python/Week_5/Tasks/Mandatory_tasks/titanic_train.csv")
print(f"{df_csv.head()}\n")
df_csv.plot(kind='hist', x='Survived', y='Fare')
#df_csv['Survived'].plot(kind='hist')
plt.show()

#Create dataframe from json
chocolate_product = """{
    "product_name": ["White chocolate 80%", "Dark chocolate 50%", "Truffle chocolate 60%", "Milk chocolate 50%", "Praline chocolate 40%"],
    "brand": ["Milka", "Hershey", "Ferrero", "KitKa", "Snickers"],
    "weight_g": [200, 100, 50, 70, 90],
    "price_$": [5, 2, 10, 6, 5]
    }"""
read_json = json.loads(chocolate_product)
print(pd.DataFrame(data=read_json), '\n')

#Create dataframe from dict
character = {
    "name": ['Roy', 'Emily', 'Kaisa', 'Fortune', 'Joe'],
    "heigh": [183, 170, 180, 175, 178],
    "weight": [62, 53, 56, 55, 65],
    "major": ['Python-Developer', 'Model', 'Chef', 'developer', 'builder']
}
df_dict = pd.DataFrame(data=character)
print(df_dict, '\n')

#Create dataframe from list
names = ['Tom', 'Mark', 'Bella', 'Stella']
ages = [20, 18, 22, 25]
emails = ['tom@mail.com', 'mark@mail.com', 'bella@mail.com', 'stella@mail.com']
data_dict = {
    'Name': names,
    'Age': ages,
    'Email': emails
}
df_list = pd.DataFrame(data=data_dict)
print(f"{df_list}\n")