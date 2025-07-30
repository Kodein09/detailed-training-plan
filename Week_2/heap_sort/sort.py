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


def build_max_heap(arr):
    pass

def heapify(arr, n, i):


array = [22, 11, 88, 66, 55, 33, 77, 44]
build_max_heap(array)
print(array)