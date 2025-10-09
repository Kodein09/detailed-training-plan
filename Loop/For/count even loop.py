nums = [2,5,8,3,10,7,6]
count = 0
for num in nums:
    if num % 2 == 0:
        print(f"Even: {num}")
        count += 1
print(f"Count of even numbers: {count}")
