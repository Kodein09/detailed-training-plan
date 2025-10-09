# def heapify(arr, n, i):
#     largest = i    # Инициализация наибольшего как основного
#     left = 2 * i + 1
#     right = 2 * i + 2
#
#     if left < n and arr[i] < arr[left]:
#         largest = left
#
#     if right < n and arr[largest] < arr[right]:
#         largest = right
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
# def heap_sort(arr):
#     n = len(arr)
#
#     for i in range(n // 2, -1, -1):
#         heapify(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#
# a = [12, 11, 13, 5, 6, 7]
# heap_sort(a)
# n = len(a)
# for i in range(n):
#     print(a[i])


# def heap_sort(arr, i, j):
#     largest = i
#     left = i * 2 + 1
#     right = i * 2 + 2
#
#     if left < j and arr[i] < arr[left]:
#         largest = left
#
#     if right < j and arr[largest] < arr[right]:
#         largest = right
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, )


# def heapify(arr, heap_size, root_index):
#     largest = root_index
#     left_child = (2 * root_index) + 1
#     right_child = (2 * root_index) + 2
#
#     if left_child < heap_size and arr[left_child] > arr[largest]:
#         largest = left_child
#
#     if right_child < heap_size and arr[right_child] > arr[largest]:
#         largest = right_child
#
#     if largest != root_index:
#         arr[largest], arr[root_index] = arr[root_index], arr[largest]
#         heapify(arr, heap_size, root_index)
#
# def heap_sort(arr):
#     array_length = len(arr)
#     for i in range(array_length, -1, -1):
#         heapify(arr, array_length, i)
#
#     for i in range(array_length - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#
# random_list_of_nums = [35, 12, 43, 8, 51, 87, 65]
# heap_sort(random_list_of_nums)
# print(random_list_of_nums)


def heapify(arr, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != root_index:
        arr[largest], arr[root_index] = arr[root_index], arr[largest]
        heapify(arr, heap_size, root_index)

def heap_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)