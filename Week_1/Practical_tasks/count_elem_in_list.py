from typing import List, Dict

# def count_elements(data: List[int]):
#     count = 0
#     for i in data:
#         count += 1
#     return count
#
# my_list = [1,2,3,4,5]
# print(count_elements(my_list))


# def count_frequency(my_list: List[int]):
#     my_dict = {}
#     for i in my_list:
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1
#
#     for key, value in my_dict.items():
#         print(f"{key}: {value}")
#     return my_dict
#
# data = [1,1,2,2,2,2,3,3,3,4,5,5,5,6,6]
# print(count_frequency(data))
#
#
# def count_letters(text: str):
#     text.lower().replace(" ", "")
#     count_dict = {}
#     for char in text:
#         if char in count_dict:
#
#             count_dict[char] += 1
#         else:
#             count_dict[char] = 1
#
#     for key, value in count_dict.items():
#         print(f"{key}: {value}")
#     return count_dict
#
# my_text = "Programming Language Python"
# count_letters(my_text)


example_of_my_text = "Abracadabra"
some_list = [1,1,1,2,2,1,1,3,13,4,5,25,25]

def count_element(list_of_elem) -> Dict:
    dict_of_elem = {}
    for i in list_of_elem:
        if i in dict_of_elem:
            dict_of_elem[i] += 1
        else:
            dict_of_elem[i] = 1

    return dict_of_elem

print(count_element(example_of_my_text))
print(count_element(some_list))
