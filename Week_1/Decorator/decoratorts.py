# Function As First-Class-Objects

# def greet(name):
#     return f"Hello, {name}. Nice to meet you."
#
# say_hello = greet
#
# def apply(a, b):
#     return a(b)
#
# res = apply(a=say_hello, b=input("Enter your name: "))
# print(res)
#
#
#
# def make_mult(f):
#     def mult(x):
#         return f * x
#     return mult
#
# dbl = make_mult(int(input("Enter your age by multiplying the numbers: ")))
# print(dbl(int(input("Enter your age by multiplying the numbers: "))))

# Function As First-Class-Objects



# Types of Decorators
# 1 Function Decorators:

# def simple_decorator(f):
#     def wrapper():
#         #print("Before calling the function.")
#         f()
#         #print("After calling the function.")
#     return wrapper
#
# @simple_decorator
# def greet_from_anel():
#     print("Hello, From Anel!")
#
# @simple_decorator
# def greet_from_roy():
#     print("Hello, From Roy to Anel!")
#
# greet_from_anel()
# greet_from_roy()


# 2 Method Decorators:

# def method_decorators(func):
#     def wrapper(self, *args, **kwargs):
#         print("Before method")
#         res = func(self, *args, **kwargs)
#         print("After method")
#         return res
#     return wrapper
#
# class MyClass:
#     @method_decorators
#     def say_hello(self):
#         print("Hello!")
#
# obj = MyClass()
# obj.say_hello()


# def method_decorator(f):
#     def wrapper(self, *args, **kwargs):
#         print("Before called f")
#         res = f(self, *args, **kwargs)
#         print("After called f")
#         return res
#     return wrapper
#
# class MyClass:
#     @method_decorator
#     def say_hello(self):
#         print("Hello")
#
# obj = MyClass()
# obj.say_hello()


# def logger(func):
#     def wrapper(self, *args, **kwargs):
#         print(f"[LOG] Function called: {func.__name__}")
#         return func(self, *args, **kwargs)
#     return wrapper
#
# class Log:
#     @logger
#     def process(self):
#         print("Processing completed")
#
# service = Log()
# service.process()


# def require_admin(func):
#     def wrapper(self, *args, **kwargs):
#         if not getattr(self, "is_admin", False):
#             raise PermissionError("Only admin can be passed")
#         return func(self, *args, **kwargs)
#     return wrapper
#
# class Dashboard:
#     def __init__(self, is_admin):
#         self.is_admin = is_admin
#
#     @require_admin
#     def delete_all(self):
#         print("All records has been deleted.")
#
# user = Dashboard(is_admin=False)
# admin = Dashboard(is_admin=True)
#
# admin.delete_all()
# user.delete_all()


# def positive_only(func):
#     def wrapper(self, value):
#         if value <= 0:
#             raise ValueError("Value must be positive.")
#         return func(self, value)
#     return wrapper
#
# class Wallet:
#     def __init__(self):
#         self.balance = 0
#
#     @positive_only
#     def add(self, amount):
#         self.balance += amount
#         print(f"Balance: {self.balance}")
#
# wallet = Wallet()
# wallet.add(2)


# def retry_once(func):
#     def wrapper(self, *args, **kwargs):
#         try:
#             return func(self, *args, **kwargs)
#         except Exception as e:
#             print(f"Error: {repr(e)}, retry...")
#             return func(self, *args, **kwargs)
#     return wrapper
#
# import random
#
# class Network:
#     @retry_once
#     def fetch(self):
#         if random.random() < 0.5:
#             raise ConnectionError("Error network!")
#         print("Receive data")
#
# net = Network()
# net.fetch()

# import webbrowser
#
# def validator(func):
#     def wrapper(url):
#         print("This text is before call func")
#         func(url)
#         print("This text is after call func")
#     return wrapper
#
# @validator
# def open_url(url):
#     webbrowser.open(url)
#
# open_url("https://www.youtube.com")

# def decorator(func):
#     def wrapper():
#         print('Before')
#         func()
#         print('After')
#     return wrapper
#
# @decorator
# def hello_wold():
#     print('Hello World!')

# from functools import wraps
#
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Before')
#         result = func(*args, **kwargs)
#         print('After')
#         return result
#     return wrapper
#
# def hello_world():
#     print('Hello World!')
#
# my_decorator(hello_world)()

# from functools import wraps
#
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Before func')
#         result = func(*args, **kwargs)
#         print('After func')
#         return result
#     return wrapper
#
# @my_decorator
# def hello(name):
#     print(f"Hello, {name}.")
#
# hello('Roy')