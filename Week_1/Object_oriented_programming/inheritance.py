# class Person:
#     def say_hello(self):
#         print("Привет, я человек")
#
# class Student(Person):
#     def study(self):
#         print("Я учусь.")
#
# student = Student()
# student.say_hello()
# student.study()
#


# class Person:
#     def __init__(self, name, age, sex, course, major):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.course = course
#         self.major = major
#
#     def greet(self):
#         return f"Hello, I write about myself below, ask for applause."
#
# class Teacher(Person):
#     def __init__(self, name, age, sex, course, major, experience):
#         super().__init__(name, age, sex, course, major)
#         self.experience = experience
#
#     def about_teacher(self):
#         return f"{super().greet()}\nMy name is {self.name}, I am {self.age} years old, I am a {self.sex}, my major is {self.major} and my teaching experience is {self.experience}."
#
# class Student(Person):
#     def __init__(self, name, age, sex, course, major, grade_average):
#         super().__init__(name, age, sex, course, major)
#         self.grade_average = grade_average
#
#     def about_student(self):
#         return f"My name is {self.name}, my age {self.age}, {self.sex}, major is {self.major} and my average grade is {self.grade_average}."
#
# teacher = Teacher("Kirusu Makise", 18, "Female", None, "Neurolog", 1)
# student = Student("Yuko Kanoie", 20, "Female", None, "Bio-engineer", "5")
# print(student.about_student())
# print(teacher.about_teacher())


# class Automobile:
#     def __init__(self, year, model, price):
#         self.year = year
#         self.model = model
#         self.price = price
#
# class Ferrari(Automobile):
#     def __init__(self, year, model, price, max_speed, engine):
#         super().__init__(year, model, price)
#         self.max_speed = max_speed
#         self.engine = engine
#
#     def info(self):
#         return f"Ferrari:\nModel: {self.model}\nYear: {self.year}\nTotal price: {self.price}$\nMax speed: {self.max_speed}km/h\nEngine type: {self.engine}"
#
# car = Ferrari(2026, "SF90 Stradale", 995000, 340, "V8-turbo")
# print(car.info())

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance
#         self.history = [balance]
#
#     def bank_account(self, amount):
#         old_balance = self._balance
#         self._balance += amount
#         self.history.append(self._balance)
#         return f"Balance replenished: {old_balance}$ + {amount}$ = {old_balance + amount}$, History: {self.history}"
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise ValueError("Can't write-off from an empty bank account")
#         old_balance = self._balance
#         self._balance -= amount
#         self.history.append(self._balance)
#         return f"Write-off: {old_balance}$ - {amount}$ = {old_balance - amount}$, History: {self.history}"
#
# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#
#     def apply_interest(self):
#         old_balance = self._balance
#         interest = int(self._balance * (self.interest_rate / 100))
#         self._balance += interest
#         self.history.append(self._balance)
#         return f"Apply Interest: {old_balance}$ * {self.interest_rate}% = {self._balance}$, History: {self.history}"
#
# class CreditAccount(Account):
#     INTEREST_BY_MONTH = {
#         3: 0.1,
#         6: 0.15,
#         9: 0.20,
#         12: 0.25
#     }
#
#     def __init__(self, owner, balance, credit_amount, months):
#         super().__init__(owner, balance)
#         self.credit_limit = 200
#         self.arbitrary_amount = credit_amount
#         self.arbitrary_month = months
#
#     def credit(self):
#         if self.credit_limit == 0:
#             raise ValueError(f"The bank has no money to issue a loan")
#
#         if self.arbitrary_amount > self.credit_limit:
#             raise ValueError(f"It is not possible to issue more than the allowed credit limit: {self.credit_limit}.")
#
#         self.credit_limit -= self.arbitrary_amount
#         old_balance = self._balance
#         self._balance += self.arbitrary_amount
#         duty = self.arbitrary_amount
#         print(f'{self.owner} received a loan in the amount of: {duty}$')
#         print(f"Current credit limit bank have: {self.credit_limit}$")
#         print(f"Source balance: {old_balance}$\nBalance after credit: {self._balance}$")
#
#         if self.arbitrary_month == 3: #10%
#             interest_rate = self.arbitrary_amount * 0.1
#             self.arbitrary_amount += interest_rate
#             print(f"You need to repay the loan with a 10% interest rate in 3 months. The total debt amount is: {self.arbitrary_amount}$")
#
#         elif self.arbitrary_month == 6: #15%
#             interest_rate = self.arbitrary_amount * 0.15
#             self.arbitrary_amount += interest_rate
#             print(f"You need to repay the loan with a 15% interest rate in 6 months. The total debt amount is: {self.arbitrary_amount}$")
#
#
#         elif self.arbitrary_month == 9: #20%
#             interest_rate = self.arbitrary_amount * 0.20
#             self.arbitrary_amount += interest_rate
#             print(f"You need to repay the loan with a 20% interest rate in 9 months. The total debt amount is: {self.arbitrary_amount}$")
#
#         else: #25% 12-month
#             interest_rate = self.arbitrary_amount * 0.25
#             self.arbitrary_amount += interest_rate
#             print(f"You need to repay the loan with a 25% interest rate in 12 months. The total debt amount is: {self.arbitrary_amount}$")
#
# # saving_acc = SavingsAccount('Roy', 100, 20)
# # print(saving_acc.bank_account(5))
# # print(saving_acc.bank_account(5))
# # print(saving_acc.withdraw(10))
# # print(saving_acc.apply_interest())
#
# credit_acc = CreditAccount('Roy', 100)
# print(credit_acc.credit())