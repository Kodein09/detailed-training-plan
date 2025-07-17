# class MyClass:
#     pass
#
# print(type(MyClass))
#
# NewClass = (type("MyNewClass", (), {"a": 1}))
# print(NewClass.mro())
# print(NewClass.a)


class MyMeta(type):
    def __new__(cls, name, base, dct):
        dct['created_by'] = 'meta'
        return super().__new__(cls, name, base, dct)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.created_by)