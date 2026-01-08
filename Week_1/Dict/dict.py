# ages = {"Alice": 20, "Bob": 23, "Garry": 21}
# print(ages["Bob"])
#
# ages["Diana"] = 24
# print(ages["Diana"])
#
# print(ages.get("Eva", "Not found"))


# nums = [1, 2, 2, 3, 1, 1, 2, 4, 3, 5]
#
# my_dict = {}
# for num in nums:
#     if num in my_dict:
#         my_dict[num] += 1
#         print(my_dict)
#     else:
#         my_dict[num] = 1
#
# print("My dict:", my_dict)

# phones = {
#     "Roy": "123-456",
#     "Eva": "643-221",
#     "Alexa": "765-432"
# }
#
# # print(phones["Alexa"])
# # phones["John"] = "987-654"
# # print(phones)
#
# phones["Roy"] = "2929-09"
# print(phones)
#
# # del phones["Eva"]
# #
# # print(phones)
#
# for name, number in phones.items():
#     print(name, "->", number)

# names = ["Рой", "Аня", "Игорь", "Рой", "Аня", "Рой"]
# result = {}
# for name in names:
#     if name in result:
#         result[name] += 1
#     else:
#         result[name] =  1
#
# print(result)

# words = ["python", "java", "python", "c++", "java", "python", "go"]
# result = {}
#
# # for language in words:
# #     result[language] = len(language)
# #
# # print(result)
#
# for lan in words:
#     result[lan] = len(set(lan))
#
# print(result)

# grades = [("math", 5), ("physics", 4), ("math", 3), ("chemistry", 5), ("physics", 2)]
# result = {}
#
# for subject, grade in grades:
#     if subject in result:
#         result[subject] += grade
#     else:
#         result[subject] = grade
#
# print(result)

#num = 0
# reversed_num = int(str(num)[::-1])
# if num == int(str(reversed_num)[::-1]):
#     print(True)
# else:
#     print(False)

# roman = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }
# s = str(input('Roman numerical: '))
# number = 0
# for letter in s:
#     for key, value in roman.items():
#         if letter == key:
#             number += value
# print(f'Here is converting roman to integer: {s} = {number}')

# roman = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }
#
# s = input('Converter roman to integer: ')
# number = 0
#
# for i in range(len(s)):
#     if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
#         number -= roman[s[i]]
#     else:
#         number += roman[s[i]]
# print(f"Result: {number}")

#Wrong
# def dupl(nums):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# print(dupl([1, 2, 3, 1]))

# def dulp(nums):
#     new_nums = set(nums)
#     if len(new_nums) < len(nums):
#         return True
#     return False
# print(dulp([1,2,3,1]))

# def dupl(nums):
#     seen = {}
#     for i in nums:
#         if i in seen:
#             return True
#         seen[i] = True
#     return False
# print(dupl([1,2,3,1]))


#Stack
# n = int(input())
# def happy_number(n):
#     first_n = n
#     list_ = []
#     while n != 0:
#         list_.append(n % 10)
#         n //= 10
#
#     for i in list_:
#         n += i**2
#         if len(list_) == 1 and 1 in list_:
#             return True
#
#         if len(list_) == 2 and first_n in list_:
#             return False
#
#     return happy_number(n)
#
# print(happy_number(7))

# def is_happy(n):
#     i = 0
#     j = 0
#     k = 0
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         i = n % 10
#         n //= 10
#         j = n % 10
#         n //= 10
#         if n:
#             k = n % 10
#             n //= 10
#             result = i**2 + j**2 + k**2
#             if result == 1:
#                 return True
#             else:
#                 n = result
#         else:
#             result = i**2 + j**2
#             if result == 1:
#                 return True
#             else:
#                 n = result
#
#     return False
#
# print(is_happy(2))

# def is_happy(n):
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = sum(int(digit)**2 for digit in str(n))
#     return n == 1
#
# print(is_happy(19))

# def majority_element(nums):
#     freq = {}
#     for value in nums:
#         if value in freq:
#             freq[value] += 1
#         else:
#             freq[value] = 1
#
#     majority = 0
#     k = 0
#     for key, value in freq.items():
#         if k < freq[key]:
#             print(f"key: {key}, value: {freq[key]}")
#             majority = key
#             k = freq[key]
#             print(majority)
#
#     return majority
# print(majority_element([2,2,1,1,1,2,2]))