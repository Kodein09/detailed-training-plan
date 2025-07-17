from itertools import count

# for i in count(10):
#     if i > 14:
#         break
#     print(i)

# for i in count(2, 2):
#     if i > 15:
#         break
#     print(i)


# def negative():
#     for i in count(5, -2.5):
#         if i < -10:
#             break
#         print(i)
#
# negative()
#
#
# def with_zip():
#     names = ["Alice", "Bob", "Gebrail"]
#     for i, name in zip(count(1), names):
#         print(i, name)
#
# with_zip()
#
#
# def id_generator():
#     return count(1)
#
# ids = id_generator()
# print(next(ids))
# print(next(ids))

# Task 1
# def task_one():
#     for i in count(5, 3):
#         if i > 20:
#             break
#         print(i)
#
# task_one()
#
# # Task 2
# def task_two():
#     students = ["Alex", "Lion", "German", "Lui", "John", "Gilbert", "Cesar"]
#     for i, name in zip(count(1), students):
#         print(i, name)
#
# task_two()
#
# # Task 3
# def task_three():
#     return count(1000)
#
# ids = task_three()
# print(next(ids))
# print(next(ids))
#
# # Task 4
# def task_four():
#     for i in count(10, -1):
#         if i < 0:
#             break
#         print(i)
#
# task_four()

# # Task 5
# def task_five():
#     my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
#     for key, value in zip(count(1), my_dict):
#         my_dict[value] **= 2
#         if key > 5:
#             break
#         print(key)
#     print(my_dict)
#
# task_five()


# def squares_value():
#     result = {}
#     for i in count(1):
#         if i > 5:
#             break
#         result[i] = i ** 2
#     print(result)
#
# squares_value()