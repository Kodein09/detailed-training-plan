num = 1234
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print(sum_digits)