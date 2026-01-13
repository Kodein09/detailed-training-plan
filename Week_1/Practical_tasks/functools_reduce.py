from functools import reduce

# initial_missing = object()
#
# def my_reduce(function, iterable, /, initial=initial_missing):
#     it = iter(iterable)
#     if initial is initial_missing:
#         value = next(it)
#     else:
#         value = initial
#     for element in it:
#         value = function(value, element)
#     return value
# print(my_reduce(lambda x, y: x*y, [1,2,3,4]))

seq = [1,2,3,4]
result = reduce(lambda x, y: x*y, seq)
print(result)