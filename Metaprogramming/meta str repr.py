class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name: {self.name} and Age: {self.age}"

    def __str__(self):
        return f"Person: {self.name}, {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person("Dave", 23)
p2 = Person("Joe", 22)
p3 = Person("Dave", 23)

print(p1 == p3)
print(p1 == p2)
print(repr(p1))
print(p2)

