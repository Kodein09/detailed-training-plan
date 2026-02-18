# a = [1,1,2,4,3,3,3,4,2,1,0,0,3]
# count = [0] * 5
# for i in a:
#     count[i] += 1
# print(count)

# s = " asdWAFawfavnbiyeahJVAOdwi 125124t zW@%#$^$%&^*"
# letters = [0] * 26
# for i in s.lower():
#     if i >= 'a' and i <= 'z':
#         number = ord(i) - 97
#         letters[number] += 1
#
# for i in range(len(letters)):
#     if letters[i] > 0:
#         print(f'{chr(i+97)} = {letters[i]}')

# import random
# a = []
# for i in range(10):
#     a.append(random.randint(-10, 10))
#
# count = [0] * 21
#
# for i in a:
#     count[i + 10] += 1
# print(a)
#
# for i in range(len(a)):
#     print(f"Negative: {i-10}, {count[i]}")


# def counting_sort(arr):
#     max_value = 4
#     count = [0] * (max_value + 1)
#
#     for num in arr:
#         count[num] += 1
#
#     sorted_arr = []
#     for i, j in enumerate(count):
#         sorted_arr.extend([i] * j)
#         print(sorted_arr)
#
#     return sorted_arr
# print(counting_sort([1,4,3,2,2,4,3,3,2,4,1,1,1,1]))

def counting_sort(arr):
    if not arr:
        return None

    max_value = max(arr)
    count_array = [0] * (max_value + 1)

    for i in arr:
        count_array[i] += 1

    for j in range(1, max_value + 1):
        count_array[j] += count_array[j - 1]

    ans = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        v = arr[i]
        ans[count_array[v] - 1] = v
        count_array[v] -= 1

    return ans

print(counting_sort([3,2,4,1]))