# class MyClass:
#     pass
#
# print(type(MyClass))
#
# NewClass = (type("MyNewClass", (), {"a": 1}))
# print(NewClass.mro())
# print(NewClass.a)


# class MyMeta(type):
#     def __new__(cls, name, base, dct):
#         dct['created_by'] = 'meta'
#         return super().__new__(cls, name, base, dct)
#
# class MyClass(metaclass=MyMeta):
#     pass
#
# print(MyClass.created_by)


# class Dog:
#     @classmethod
#     def create(cls, name):
#         return cls(name)

# class MyMeta(type):
#     def __new__(cls, name, bases, attrs):
#         """
#         :param name: name of the future class
#         :param bases: parents classes
#         :param attrs: attributes of the future class
#         """
#         return super().__new__(cls, name, bases, attrs)

class Point:
    max_coord = 100
    min_coord = 0

a = type('Point', (), {"max_coord": 100, "min_coord": 0})
print(a)

pt = a()
print(pt)
print(type(pt))

print(pt.max_coord)
print(pt.min_coord)

class B1:
    pass

class B2:
    pass

a = type("Point", (B1, B2), {})
b = B1()