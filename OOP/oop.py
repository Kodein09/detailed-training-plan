# class House:
#     """House description"""
#     def __init__(self, street, number):
#         """House properties"""
#         self.street = street
#         self.number = number
#         self.age = 0
#         self.structure = "Monolith"
#
#     def build(self):
#         """Build house"""
#         print(f"House on the street {self.street} under the number {self.number} was built")
#
#     def year_of_house(self, year):
#         """year of the house"""
#         self.age += year
#
# h = House("Gogol", 19)
# h.build()
# h.year_of_house(10)
#
# class Skyscraper(House):
#     def __init__(self, name, prospect, number, meters, floors):
#         super().__init__(self, number)
#         self.name = name
#         self.prospect = prospect
#         self.meters = meters
#         self.floors = floors
#
#     def skyscraper_height(self):
#         print(f"{self.name} this Skyscraper has {self.meters} meters high.")
#
# skyscraper = Skyscraper("Nurlytau","Alfarabi", 189, 469, 40)
# skyscraper.skyscraper_height()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Привет, меня зовут {self.name}, мне {self.age} лет."
#
#     def compare_age(self, other_person):
#         if self.age > other_person.age:
#             print(f"{self.name} older {other_person.name}")
#         elif self.age < other_person.age:
#             print(f"{self.name} younger {other_person.name}")
#         else:
#             print(f"{self.name} и {other_person.name} равны")
#
#
# p1 = Person("Alice", 21)
# p2 = Person("Bob", 22)
# print(p1.greet())
# print(p2.greet())
# p1.compare_age(p2)


# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#     def compare_year(self, other_car):
#         if self.year > other_car.year:
#             print(f"{self.model} newest than {other_car.model}")
#         elif self.year < other_car.year:
#             print(f"{self.model} oldest than {other_car.model}")
#         else:
#             print(f"{self.model} they are the same age {other_car.year}")
#
# car = Car("Huracan", 2008)
# car2 = Car("Urus", 2018)
# car.compare_year(car2)


# class Garage:
#     def __init__(self):
#         self.cars = []
#
#     def add_car(self, car):
#         self.cars.append(car)
#
#     def show_all(self):
#         for car in self.cars:
#             car.info()
#
# class Vehicle:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#     def info(self):
#         print(f"Model: {self.model}, Year: {self.year}")
#
# class ElectricCar(Vehicle):
#     def __init__(self, model, year, battery_capacity):
#         super().__init__(model, year)
#         self.battery_capacity = battery_capacity
#
#     def info(self):
#         super().info()
#         print(f"Battery capacity: {self.battery_capacity}")
# electric = ElectricCar("Tesla Model s", 2022, 100)
#
#
# electric.info()
#
# garage = Garage()
# garage.add_car(Vehicle("Ferrari", 2016))
# garage.add_car(Vehicle("Pagani", 2024))
# garage.show_all()


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def describe(self):
#         return f"Book: {self.title}, author: {self.author}, year: {self.year}"
#
# book = Book("48 Законов Власти", "Роберт Грин", 1998)
# book2 = Book("Algorithm", "Thomas Kormen", 2009)
# print(book.describe())
# print(book2.describe())


# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
#
#     def deposit(self, amount):
#         self.__balance += amount
#         return self.__balance
#
#     def withdraw(self, amount):
#         if amount == 0:
#             ValueError("Can't withdraw, balance is zero")
#         self.__balance -= amount
#         return self.__balance
#
#     def get_balance(self):
#         return self.__balance
#
# credit_card = BankAccount()
# print(credit_card.deposit(100))
# print(credit_card.withdraw(50))
# print(credit_card.get_balance())


# import json
#
# class CountryData:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.file_data = self.read_file()
#         self.max_temp = self.file_data["max_temp"]
#         self.min_temp = self.file_data["min_temp"]
#         self.country = self.file_data["Country"]
#
#     def read_file(self):
#         with open(self.file_path, 'r') as country_file:
#             return json.load(country_file)
#
# egypt = CountryData('')
# print(egypt.file_data)
# print(f"Country: {egypt.country}")
# print(f"Max summer temperature in {egypt.country}: {egypt.max_temp}")
# print(f"Min winter temperature in {egypt.country}: {egypt.min_temp}")
# print(f"Sum of temperature: {egypt.max_temp + egypt.min_temp}")


# class Employer:
#     def __init__(self, name, job, salary):
#         self.name = name
#         self.job = job
#         self.salary = salary
#
#     def change_salary(self, new_salary):
#         self.salary = new_salary
#         return f"New Salary {self.salary} for {self.name}"
#
#     def employer_info(self):
#         return f"Name: {self.name}, Job: {self.job}, Salary: {self.salary}"
#
# emp = Employer("Augustin", "Designer", 200_000)
# emp2 = Employer("Angelica", "Dancer", 100_000)
# print(emp.employer_info())
# print(emp2.employer_info())
#
#
# class RemoteEmployer(Employer):
#     def __init__(self, name, job, salary, country):
#         super().__init__(name, job, salary)
#         self.country = country
#
#     def remote_info(self):
#         return f"Employer from {self.country} his name is - {self.name}"
#
#     def employer_info(self):
#         return f"Employer name: {self.name}, job: {self.job}, salary: {self.salary} and his country is: {self.country}"
#
# remote = RemoteEmployer("Max", "Player", 90_000, "Korea")
# print(remote.employer_info())
#
#
#
# from abc import ABC, abstractmethod
#
# class EmployeeBase(ABC):
#     @abstractmethod
#     def get_role(self):
#         pass
#
#     def greet(self):
#         return f"Hi, I'm work as a {self.get_role()}"
#
# class Manager(EmployeeBase):
#     def get_role(self):
#         return "manager"
#
# e = EmployeeBase()


# from abc import ABC, abstractmethod
#
# class Employee(ABC):
#     @abstractmethod
#     def get_role(self):
#         pass
#
#     def greet(self):
#         return f"Hi, I'm work as a {self.get_role()}"
#
# class Manager(Employee):
#     def get_role(self):
#         return "manager"
#
# s = Employee()
# print(s.greet())


# from  abc import ABC, abstractmethod
#
# class Employee(ABC):
#     @abstractmethod
#     def get_role(self):
#         pass
#
#     def greet(self):
#         return f"Hi, I'm a {self.get_role()}"
#
# class Manager(Employee):
#     def get_role(self):
#         return "manager"
#
# class Engineer(Employee):
#     def get_role(self):
#         return "engineer"
#
# class Designer(Employee):
#     def get_role(self):
#         return "designer"
#
# class Janitor(Employee):
#     def get_role(self):
#         return "janitor"
#
# class HR(Employee):
#     def get_role(self):
#         return "hr"
#
# class Developer(Employee):
#     def get_role(self):
#         return "developer"
#
# class QA(Employee):
#     def get_role(self):
#         return "qa"
#
# class Support(Employee):
#     def get_role(self):
#         return "support"
#
# class Intern(Employee):
#     def get_role(self):
#         return "intern"
#
# class Director(Employee):
#     def get_role(self):
#         return "director"
#
# manager = Manager()
# engineer = Engineer()
# qa = QA()
# hr = HR()
# supp = Support()
# intern = Intern()
# director = Director()
# designer = Designer()
# developer = Developer()
# janitor = Janitor()
#
# employee = [manager, engineer, developer, director, janitor, designer, intern, supp, hr, qa]
#
# for i in employee:
#     print(i.greet())


# from abc import abstractmethod
# class Shape:
#     @abstractmethod
#     def draw(self):
#         return 'shapes'
#
# class Circle(Shape):
#     super().draw()
#     def draw(self):
#         return 'circle'
#
# class Square(Shape):
#     super().draw()
#     def draw(self):
#         return 'square'
#
# class Triangle(Shape):
#     super().draw()
#     def draw(self):
#         return 'triangle'


# class User:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if not value:
#             raise ValueError("Name cannot be empty")
#         self._name = value
#
# user = User("Roy")
# print(user.name)


# class Product:
#     def __init__(self, price):
#         self._price = price
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, value):
#         if not value:
#             raise ValueError("Price cannot be empty")
#         elif value < 0:
#             raise ValueError("Price cannot be negative")
#         self._price = value
#
# product = Product(20.00)
# print(product.price)


import re

class SuperMarket:
    def __init__(self, employer, product, price):
        self.__name = employer
        self.__product = product
        self.__price = price

    @property
    def employer(self):
        return self.__name

    @employer.setter
    def employer(self, value):
        if re.fullmatch(r'[a-zA-Z]', value):
            print("Valid name")
        else:
            print("Invalid name")
        self.__name = value

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        if not value:
            raise ValueError("Product name cannot be empty.")
        elif re.fullmatch(r'[a-zA-Z]', value):
            print("Valid product name")
        self.__product = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value == r'a-zA-Zа-яА-Я':
            raise ValueError("Only digits can be passed for price.")
        self.__price = value

supermarket = SuperMarket("Anel", "Ring", 12_000)
print(supermarket.employer)
print(supermarket.product)
print(supermarket.price)