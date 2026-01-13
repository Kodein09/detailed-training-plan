# def linear_search_return_all_indexes(array, target):
#     all_indexes = []
#     find_target = 0
#     for i in range(len(array)):
#         all_indexes.append(i)
#         if array[i] == target:
#             find_target = array[i]
#             continue
#     return f"Target: {find_target}\nAll indexes: {all_indexes}"
# print(linear_search_return_all_indexes([62,37,12,86,9,34,85,96], 9))


def linear_search_all_indexes(a, x):
    all_position_where_x = []
    for i in range(len(a)):
        if a[i] == x:
            all_position_where_x.append(i)
            continue
    return f"All position for target value: {all_position_where_x}"
print(linear_search_all_indexes([62,37,12,86,9,34,85,96,9,100,19,9], 9))