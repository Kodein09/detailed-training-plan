num = 123
reverse = 0
while num > 0:
    reverse = reverse * 10 + (num % 10)
    num //= 10
print(reverse)