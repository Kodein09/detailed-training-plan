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