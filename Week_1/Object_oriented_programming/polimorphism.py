# class Person:
#     def __init__(self, name, age, sex, course, major):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.course = course
#         self.major = major
#
#     def greet(self):
#         return f"Hello and Welcome, I write about myself below, ask for applause."
#
#     def introduce(self):
#         return f"I am a Human, I am a Person, I am.. a {self.name}."
#
# class Teacher(Person):
#     def __init__(self, name, age, sex, course, major, experience):
#         super().__init__(name, age, sex, course, major)
#         self.experience = experience
#
#     def introduce(self):
#         return f"I am a Teacher"
#
#     def about_teacher(self):
#         return f"My name is {self.name}, I am {self.age} years old, I am a {self.sex}, my major is {self.major} and my teaching experience is {self.experience}."
#
# class Student(Person):
#     def __init__(self, name, age, sex, course, major, grade_average):
#         super().__init__(name, age, sex, course, major)
#         self.grade_average = grade_average
#
#     def introduce(self):
#         return f"I am a student"
#
#     def about_student(self):
#         return f"My name is {self.name}, my age {self.age}, {self.sex}, major is {self.major} and my average grade is {self.grade_average}."
#
# peoples = [Student("Roy", 20, "Male", 4, "MLOps", 3),
#           Teacher("Anel", 20, "Female", None, "Teacher of Design", 1)]
# for people in peoples:
#     print(people.introduce())

from datetime import datetime

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.transaction = []

    def _log(self, operation, amount):
        record = {
            'Operation': operation,
            'Amount': amount,
            'Balance': self._balance,
            'Time': datetime.now()
        }
        print(type(record['Balance']))
        return record

    def replenishment(self, amount):
        self._balance += amount
        return self._log('Replenishment', amount)

    def withdrawal(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds to withdraw.")
        self._balance -= amount
        self._log('Withdrawal', amount)

acc = Account('Roy', 0)
print(acc.replenishment(100))

class SavingsAccount(Account):
    def __init__(self, owner, balance, deposit):
        super().__init__(owner, balance)
        self.deposit = deposit

    def _log(self, operation, amount):
        records = {
            'Operation': operation,
            'Amount': amount,
            'Deposit': self.deposit,
            'Time': datetime.now()
        }
        self.transaction.append(records)
        return records

    def deposit_replenishment(self, amount):
        self.deposit += amount
        return self._log('Deposit replenishment', amount)

    def deposit_withdrawal(self, amount):
        if amount > self.deposit:
            raise ValueError("The withdrawal amount exceeds the deposit amount.")

        self._balance += self.deposit
        self.deposit -= amount
        return self._log('Withdrawal from deposit', amount)

class CreditAccount(Account):
    def __init__(self, owner, balance, credit_limit=200):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def _log(self, operation, amount):
        records = {
            'Operation': operation,
            'Amount': amount,
            'Balance': self._balance,
            'Time': datetime.now()
        }
        self.transaction.append(records)
        return records

    def withdrawal(self, amount):
        if amount > self.credit_limit:
            raise ValueError("Credit limit exceeded")
        self.credit_limit -= amount
        self._balance += amount
        return self._log('Loan', amount)