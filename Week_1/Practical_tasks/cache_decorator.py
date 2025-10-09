# from functools import lru_cache
#
# @lru_cache(maxsize=10)
# def test_num(num):
#     result = 0
#     for i in range(num):
#         result += 1
#     return result
#
# n = test_num(10000000)
# print(n)
# print(n)
# print(n)
# print(n)
# print(n)
# print(n)

# def test_num(n):
#     dict_cache = {}
#     for i in range(n):
#         if i in dict_cache:
#             return i
#         else:
#             dict_cache[i] = n

def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            return cache[key]

        result = func(*args, *kwargs)
        cache[key] = result
        return result
    return wrapper

@memoize
def test_num(n):
    result = 0
    for i in range(n):
        result += 1
    return result
print(test_num(100000000))
print(test_num(100000000))
print(test_num(100000000))
print(test_num(100000000))
print(test_num(100000000))
