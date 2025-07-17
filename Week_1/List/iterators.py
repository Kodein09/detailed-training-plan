#List comprehension Генераторы списков лаконичный и быстрый способ создать новый итерируемый спискок

# # squares = []
# # for i in range(7):
# #     squares.append(i * i)
# #     print(squares)
#
#
# even = [i for i in range(10) if i % 2 == 0]
# print(even)
#
# not_even = [i for i in range(10) if i % 2 == 1]
# print(not_even)


# squares = [i * i for i in range(1, 11) if i % 2 == 1]
# print(squares)
#
# res = [i for i in range(5) if i != 2]
# print(res)

# my_iter = [10, 20, 30]
# it = iter(my_iter)
# print(next(it))
# print(next(it))
# print(next(it))

# my_list = [1,2,3,4,5,6,7,8]
# it = (i for i in range(len(my_list)) if i % 2 == 1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# Итоги: Что такое итератор?
# Итератор это объект в Python, по которому можно пройтись по одному элементу за раз
# По признакам можно понять, что является итератором:
# Имеются методы iter и next __iter__(), __next__()
# Можно использовать в цикле for
# Можно вызвать вручную по __next__()
# Пример ниже:
# my_list = [1,2,3,4,5]
# it = iter(my_list)
# print(next(it))
# print(next(it))


# Генераторы списков является короткой формой записи создания нового списка из другого списка
# Пример ниже:
#squares = [i * i for i in range(6)]
#print(squares)
# Можно после цикла добавить условие, к примеру на поиск чётных или нечётных чисел
# even = [i for i in range(7) if i % 2 == 0]
# print(even)
#
# not_even = (i for i in range(8) if i % 2 == 1)
# it = iter(not_even)
# print(next(it))
# print(next(not_even))
#
# print(help())


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

palindrome = "A man a plan a canal Panama"

cleaned = ''.join(c.lower() for c in palindrome if c.isalnum())
for char in Reverse(cleaned):
    print(char, end='')

def is_palindrome(text):
    reversed_text = text == cleaned
    return reversed_text

print('\n', is_palindrome(cleaned))
