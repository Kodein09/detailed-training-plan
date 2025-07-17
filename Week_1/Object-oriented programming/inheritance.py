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