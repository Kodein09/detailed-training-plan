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
