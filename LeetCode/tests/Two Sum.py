def two_sum(numbers, target):

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]

nums = [1, 2, 5, 7, 11]
x = 9

result = two_sum(nums, x)
print(result)