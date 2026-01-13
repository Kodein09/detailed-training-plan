# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     a, b = 0, 1
#     while n > 0:
#         a, b = b, a + b
#         n -= 1
#     return a
# print(fibonacci(5))

# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
# print(fibonacci(5))


from functools import lru_cache
"""
По сути то же, что и memoization (могу ошибаться)
LRU - Least Recently Used
Param:
user_function = пользовательская функция
maxsize = тип int, максимальный размер кеша
typed = bool, кэшировать при разных типах аргументов
возвращаемое значение будет результатом пользовательской функции user_function
"""
#cache = lru_cache(fibonacci(10))

#Or use decorator
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))
"""
Декоратор @lru_cache модуля functools оборачивает функцию с переданными в неё аргументами и запоминает возвращаемый результат.
Это экономит время и ресурсы, функция может быть достаточно дорогой, чтобы каждый раз её использовать, поэтому кэширование хорошо сюда подходит.
Для того, чтобы сработал декоратор @lru_cache необходимо, чтобы передаваемые данные аргументами в функцию были хешируемыми, т.к. для кеширования
результатов декоратор использует словарь.
"""

from time import perf_counter

#Running func time
def memorize(func):
    memoization = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in memoization:
            return memoization[key]

        result = func(*args, **kwargs)
        memoization[key] = result
        return result
    return wrapper

#Memoization
@memorize
def func(a):
    return a**2

#Execution time
start = perf_counter()
func(12)
end = perf_counter()
print(f"Execution time of 12: {end - start:.10f}\n")

#Execution time
start = perf_counter()
func(10)
end = perf_counter()
print(f"Execution time of 10: {end - start:.10f}\n")

start = perf_counter()
func(10)
end = perf_counter()
print(f"Execution time of 10: {end- start:.10}")

from functools import lru_cache

@lru_cache(maxsize=128)
def math(a, b):
    return a * b

result = math(10, 5).bit_count()
print('Bit count:', result)