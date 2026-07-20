import unittest

# def radix_sort(arr, n, max_len):
#     '''
#     :param arr: array (список)
#     :param n: количество возможных значений одного разряда
#     :param max_len: максимальное количество разрядов
#     Циклически обходим каждый разряд,
#     для каждого разряда создаём корзины.
#     В зависимости от разряда добавляем число в один из 10 списков.
#     '''
#     for i in range(max_len):    # сколько разрядов, столько раз и обходим.
#         arrays = [[] for i in range(n)]    # создаём столько пустых списков, сколько возможных значений.
#         for j in arr:
#             arrays[(j // 10**i) % n].append(j)    # по значениям добавляем числа в определённый список.
#         a = []
#         for section in arrays:
#             a.extend(section)    # последовательно объединяем списки (корзины)
#             arr = a
#
#     return arr
#
# radix = radix_sort([10, 20, 40, 3, 2, 8], 10, 5)
# print(radix)


# def counting_sort_for_radix(arr, exp):
#     array_length = len(arr)
#     output = [0] * array_length
#     count = [0] * 10
#
#     for i in range(array_length):
#         index = (arr[i] // exp) % 10
#         count[index] += 1
#
#     for i in range(1, 10):
#         count[i] += count[i - 1]
#
#     i = array_length - 1
#     while i >= 0:
#         index = (arr[i] // exp) % 10
#         output[count[index] - 1] = arr[i]
#         count[index] -= 1
#         i -= 1
#
#     for i in range(array_length):
#         arr[i] = output[i]
#
# def radix_sort(arr):
#     max_num = max(arr)
#     exp = 1
#
#     while max_num // exp > 0:
#         counting_sort_for_radix(arr, exp)
#         exp *= 10
#
# data = [170, 45, 75, 90, 802, 24, 2, 66]
# radix_sort(data)
# print(data)


# class RadixSort:
#     def counting_sort(self, arr):
#         if not arr:
#             return None
#
#         max_value = max(arr)
#         count_array = [0] * (max_value + 1)
#
#         for i in arr:
#             count_array[i] += 1
#
#         ans = [0] * len(arr)
#
#         for j in range(len(arr) - 1, -1, -1):
#             ans[count_array[j] - 1] = j
#             count_array[j] -= 1
#
#
#         return arr
#
#     def radix_sort(self, arr):
#         pass


# class RadixSort:
#     def counting_sort(self, arr, exp):
#         if not arr:
#             return None
#
#         output = [0] * len(arr)
#         count = [0] * 10
#
#         for num in arr:
#             digit = (num // exp) % 10
#             count[digit] += 1
#
#         for i in range(1, 10):
#             count[i] += count[i - 1]

def counting_sort(arr: list, exp: int) -> list:
    count = [0] * 10
    output = [0] * len(arr)

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        current_value = arr[i]
        digit = (current_value // exp) % 10
        count[digit] -= 1
        new_pos = count[digit]
        output[new_pos] = current_value

    return output

def radix_sort(arr: list) -> list:
    if not arr:
        return []

    max_value = max(arr)
    exp = 1

    while (max_value // exp) % 10 > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr

array = [12, 198, 124, 3, 25, 78]
print(radix_sort(array))