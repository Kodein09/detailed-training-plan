# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance
#
#     def deposit(self, amount):
#         self._balance += amount
#
#     def withdraw(self, amount):
#         self._balance += amount


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
#         self.__experience = experience
#
#     def introduce(self):
#         return f"I am a Teacher"
#
#     def about_teacher(self):
#         return f"My name is {self.name}, I am {self.age} years old, I am a {self.sex}, my major is {self.major} and my teaching experience is {self.__experience}."
#
# class Student(Person):
#     def __init__(self, name, age, sex, course, major, grade_average):
#         super().__init__(name, age, sex, course, major)
#         self.__grade_average = grade_average
#
#     def introduce(self):
#         return f"I am a student"
#
#     def get_grade(self):
#         return self.__grade_average
#
#     def set_grade(self, new_grade):
#         if 0 <= new_grade <= 5:
#             self.__grade_average = new_grade
#         else:
#             print("Error: digit must be an integer")
#         return new_grade
#
#     def about_student(self):
#         return f"My name is {self.name}, my age {self.age}, {self.sex}, major is {self.major} and my average grade is {self.__grade_average}."
#
# peoples = [Student("Roy", 20, "Male", 4, "MLOps", 3),
#           Teacher("Anel", 20, "Female", None, "Teacher of Design", 1)]
# for people in peoples:
#     print(people.introduce())
#
#
# student = Student("Roy", "20", None, None, None, 4.6)
# print(student.about_student())
# print(student.get_grade())
# student.set_grade(5)
# print(student.get_grade())
# student.set_grade(10)
#
# teacher = Teacher("Anel", 20, "Female", None, None, 1)
# print(teacher.about_teacher())
