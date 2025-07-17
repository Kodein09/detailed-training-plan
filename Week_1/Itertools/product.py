from itertools import product

example = 'ABCD'
pr = product(example, repeat=2)
print(next(pr))
print(next(pr))
print(next(pr))
print(next(pr))
print(next(pr))
print(next(pr))