# from collections import defaultdict
#
# words = ["apple", "banana", "apricot", "blueberry", "cherry"]
#
# grouped = defaultdict(list)
#
# for word in words:
#     first_letter = word[0]
#     grouped[first_letter].append(word)
#
# print(grouped)
#
#
# words = ["hi", "hello", "world", "ok", "no", "yes"]
#
# words_by_len = defaultdict(list)
#
# for word in words:
#     word_len = len(word)
#     words_by_len[word_len].append(word)
#
# print(words_by_len)
#
#
# words = ["apple", "angle", "grape", "bike", "spike", "stone"]
#
# word_by_last_letter = defaultdict(list)
#
# for word in words:
#     last_letter = word[-1]
#     word_by_last_letter[last_letter].append(word)
#
# for key in word_by_last_letter:
#     word_by_last_letter[key].sort()
#
# print(word_by_last_letter)

# from collections import defaultdict
# import json
#
# tree = lambda: defaultdict(tree)
#
# my_dict = tree()
# my_dict['Porsche']['panamera'] = '10_000'
# my_dict['Porsche']['911'] = '30_000'
# my_dict['Porsche']['Spider'] = '40_000'
# print(my_dict)
# print(json.dumps(my_dict), end='$')
