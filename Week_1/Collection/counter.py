from collections import Counter

# colours = (
#     ("Anel", "Pink"),
#     ("Roy", "Blue"),
#     ("Roy", "Black"),
#     ("Roy", "Red Wine"),
#     ("Ilya", "Black"),
#     ("Arif", "Pink"),
#     ("Arif", "Green")
# )
#
# my_dict = {
#     "Group 1": {"Class a": 89, "Class b": 90, "Class C": 86}, "Group 2": {"Class A": 2}, "Group 3": {"C": 3}
# }
# print(my_dict)
# print(colours)
# print(type(colours))
#
# count_favorite = Counter(name for name, colour in colours)
# print(count_favorite)


# favorite_colour = {"Roy": "Purple", "Anel": "Pink", "Arif": "Pink", "Max": "Pink"}
# fav_colour = Counter(favorite_colour.values())
# print(fav_colour)

# text = "gadadadawvawwfwagfggrgebqaaawrwqeqaqweqrgvnbv;mcapaaavzkbix"
# print(Counter(text))

# my_list = ["Alfa", "Romeo", "Lamba", "Lamba", "Romeo"]
# print(Counter(i for i in my_list))

# nums = [1,2,1,1,2,2,3]
# my_dict = {}
# for num in nums:
#     if num in my_dict:
#         my_dict[num] += 1
#         print("My Dict:", my_dict)
#         print("Index:", my_dict[num])
#     else:
#         my_dict[num] = 1
#
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
# print(my_dict)
# print(my_dict[2])
# print(my_dict[3])

# text = """
# Abracadabra, abracadabra
# Abracadabra, abracadabra
# Pay the toll to the angels
# Drawin' circles in the clouds
# """
#
# def word_frequency_analysis(lyrics):
#     word = lyrics.lower().split()
#     return Counter(word)
#
# print(word_frequency_analysis(text))

