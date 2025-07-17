class Person:
    def __init__(self, name, age, sex, course, major):
        self.name = name
        self.age = age
        self.sex = sex
        self.course = course
        self.major = major

    def greeting(self):
        return f"Hello, my name is {self.name}, {self.age} years old. I am a {self.sex}, my major is {self.major}."

class Teacher(Person):
    def about_teacher(self):
        return f"{super().greeting()} I also graduated harvard with honors."

class Student(Person):
    def about_student(self):
        return f"{super().greeting()} And I like watch the sky."

teacher = Teacher("Mia Akatsuki", "22", "Female", "graduated", "Math, Physic")
student = Student("Haruhi Shinoui", "19", "Female", 3, "Astronomy")
print(teacher.about_teacher())
print(student.about_student())