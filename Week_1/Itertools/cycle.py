from itertools import cycle

# nums = [1,2,3]
# cycler = cycle(nums)
#
# for _ in range(10):
#     print(next(cycler))
#
#
# players = ["Alice", "Bob", "Carol"]
# cycler = cycle(players)
#
# for name in range(8):
#     print("Ход игрока:", next(cycler))


# nums = [0, 1]
# cycler = cycle(nums)
#
# for i in range(12):
#     print(next(cycler))


# text = "AB"
# cycler = cycle(text)
#
# for char in range(7):
#     print(next(cycler))


# steps = ["Влево", "Вправо"]
# cycler = cycle(steps)
#
# for step in range(6):
#     print(next(cycler))


# nums = [10, 20, 30]
# cycler = cycle(nums)
# i = 0
# nums_len = len(nums)
#
# for index in range(1, 10):
#     value = next(cycler)
#     print(f"{i}, {value}")
#     i += 1
#     if i == nums_len:
#         i = 0


# switch = ["on", "off"]
# cycler = cycle(switch)
#
# for i in range(5):
#     print(next(cycler))


# players = ["Tom", "Jerry"]
# cycler = cycle(players)
#
# for i in range(5):
#     i += 1
#     print(next(cycler), "Получил карту:", i)


# plus_and_minus = ["+", "-"]
# cycler = cycle(plus_and_minus)
#
# for i in range(10):
#     print(next(cycler), end='')


# matrix = [0, 1]
# cycler = cycle(matrix)
#
# for i in range(3):
#     for j in range(4):
#         print(next(cycler), end='')
#     print()