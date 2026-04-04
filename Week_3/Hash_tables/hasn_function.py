# my_hash_set = [None, None, None, None, None, None, None, None, None, None]

# Find index of a name using hash function
# def hash_function(value):
#     sum_of_chars = 0    # Объявляю переменную для суммирования символов в ASCII
#
#     for char in value:    # Далее для каждого символа в строке
#         sum_of_chars += ord(char)    # Суммирую каждый символ при помощи build-in method ord(), который позволяет конвертировать символ в цифры от ASCII
#
#     return sum_of_chars % 10    # Далее возвращаем остаток от деления для распределения в хэш-таблицу распределяя по индексам 0-9
#
# print(f"Bob has hash code: {hash_function('Bob')}")

# def hash_function(value):
#     sum_of_chars = 0
#
#     for char in value:
#         sum_of_chars += ord(char)
#
#     return sum_of_chars % 10
# print(f"Roy has hash code: {hash_function('Roy')}")

# My little improvisation:
# def hash_function(value):
#     sum_of_chars = 0
#     hash_table = []
#
#     for char in value:
#         sum_of_chars += ord(char)
#
#     hash_table.insert(sum_of_chars % 10, value)
#
#     return hash_table
# print(hash_function('Roy'))


# Looking up a name using hash function
# my_hash_set = [None, 'Alexa', 'Jane', None, 'Roy', None, None, 'Siri', None, None]
#
# def hash_function(value):
#     sum_of_chars = 0
#
#     for char in value:
#         sum_of_chars += ord(char)
#
#     return sum_of_chars % 10
#
# def contain(name):
#     index = hash_function(name)
#     return my_hash_set[index] == name
#
# print(hash_function('Alexa'))
# print(hash_function('Siri'))
# print(hash_function('Jane'))
# print(f"Roy is in the hash set: {contain('Roy')}")
# print(f"Roy is in the hash set: {contain('Jane')}")
# print(f"Roy is in the hash set: {contain('Lara')}")


# Handling collisions
# my_hash_set = [
#     [None],
#     [None],
#     [None],
#     ['Lisa', 'Stuart'],    # Сделать метод цепочек, превратить в массив или связный список
#     ['Roy'],
#     [None],
#     [None],
#     ['Siri'],
#     [None],
#     [None]
# ]

# Hash Set example and simulation

# my_hash_set = [
#     [None],
#     ['Jones'],
#     [None],
#     ['Lisa'],
#     [None],
#     ['Bob'],
#     [None],
#     ['Siri'],
#     ['Pete'],
#     [None]
# ]
#
# def hash_function(value):
#     sum_of_chars = 0
#
#     for char in value:
#         sum_of_chars += ord(char)
#
#     return sum_of_chars % 10
#
# def contain(name):
#     index = hash_function(name)
#     bucket = my_hash_set[index]
#     return name in bucket
#
# def add(value):
#     index = hash_function(value)
#     bucket = my_hash_set[index]
#     if value not in bucket:
#         bucket.append(value)
#
# add('Roy')
#
# print(my_hash_set)
# print(f"Hash set contain Roy: {contain('Roy')}")
# add('Stuart')
# add('Jane')
# print(my_hash_set)
# add('Kayle')
# print(my_hash_set)

class HashTable:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        res = sum(ord(char) % self.capacity for char in key)
        print(res)

    def _build_in_hash(self, key):
        return hash(key) % self.capacity

ht = HashTable(5)
ht._hash('World')