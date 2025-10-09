numbers = [5, 8, 3, 10, 6, 2, 7]
total = 0

for num in numbers:
    if total + num > 20:
        continue
    total += num

print(total)

