# def quick_sort(arr, left, right):
#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quick_sort(arr, left, partition_pos - 1)
#         quick_sort(arr, partition_pos + 1, right)
#
#
# def partition(arr, left, right):
#     i = left
#     j = right - 1
#     pivot = arr[right]
#
#     while i < j:
#         while i < right and j < arr[i] < pivot:
#             i += 1
#         while j > left and arr[j] >= pivot:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#     if arr[i] > pivot:
#         arr[i], arr[right] = arr[right], arr[i]
#
#     return i
#
#
# arr = [22, 11, 88, 66, 55, 77, 33, 44]
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)


# def quicksort(arr, left, right):
#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quicksort(arr, left, partition_pos - 1)
#         quicksort(arr, partition_pos + 1, right)
#
# def partition(arr, left, right):
#     i = left
#     j = right
#     pivot = arr[right]
#
#     while i < j:
#         while i < right and j < arr[i] < pivot:
#             i += 1
#
#         while j > left and arr[j] >= pivot:
#             j -= 1
#
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#     if arr[i] > pivot:
#         arr[i], arr[right] = arr[right], arr[i]
#
#     return i
#
# a = [22, 11, 55, 77, 33, 88, 66, 44]
# quicksort(a, 0, len(a) - 1)
# print(a)


# def quicksort(arr, left, right):
#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quicksort(arr, left, partition_pos - 1)
#         quicksort(arr, partition_pos + 1, right)
#
# def partition(arr, left, right):
#     i = left
#     j = right
#     pivot = arr[right]
#
#     while i < j:
#         while i < right and j < arr[i] < pivot:
#             i += 1
#
#         while j > left and arr[j] >= pivot:
#             j -= 1
#
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#
#         if arr[i] > pivot:
#             arr[i], arr[right] = arr[right], arr[i]
#
#     return i
#
# a = [22, 11, 88, 33, 55, 77, 66, 44]
# quicksort(a, 0, len(a) - 1)
# print(a)


# def quicksort(arr, left, right):
#     if left < right:
#         partition_pos = partition(arr, left, right)
#         quicksort(arr, left, partition_pos - 1)
#         quicksort(arr, partition_pos + 1, right)
#
# def partition(arr, left, right):
#     i, j, pivot = left, right, arr[right]
#     print(i, j, pivot)
#
#     while i < j:
#         while i < right and j < arr[i] < pivot:
#             print(f"i: {i}\nj: {j}\narr[i]: {arr[i]}\npivot: {pivot}")
#             i += 1
#
#         while j > left and arr[j] >= pivot:
#             print(j)
#             j -= 1
#
#         if i < j:    # Если индекс i меньше индекса j (а j идёт от конца списка (слева от pivot), не считая последний элемент pivot, то j всегда больше i) выполняем перестановку элементов
#             arr[i], arr[j] = arr[j], arr[i]
#
#         if arr[i] > arr[right]:
#             arr[i], arr[right] = arr[right], arr[i]
#
#     return i
#
# a = [22, 11, 55, 77, 33, 88, 44]
# print(partition(a, 0, len(a) - 1))
# print(a)


# def quicksort(arr, left, right):
#     if left < right:
#         pivot_pos = partition(arr, left, right)
#         quicksort(arr, left, pivot_pos - 1)    # Подмассив sub-array начинающий от левой части 0 до опорной части - 1 (pivot - 1) все элементы, которые меньше чем значение элемента pivot: elements < p
#         quicksort(arr, pivot_pos + 1, right)    # Подмассив sub-array правая его часть, от опорной части + 1 следующий элемент (pivot + 1) до правой части, которые больше опорного элемента: elements > p
#
# def partition(arr, left, right):
#     i = left    # Левая часть - начало = 0
#     j = right - 1    # Предпоследний элемент, если считать от массива и от pivot элемента, либо, слева стоящий от опорного элемента pivot.
#     pivot = arr[right]    # Последний элемент массива и подмассива.
#
#     while i < j:    # Пока i < j они не пересеклись, потому что от начала массива идёт i и j от предпоследнего значения, либо, слева от pivot мы будем выполнять то, что идёт ниже внутри цикла.
#         while i < right and j < arr[i] < pivot:    # Пока i не находится в конце массива (right) И элемент с индексом i меньше чем pivot увеличиваем i.
#             i += 1    # Начнём с перемещения i вправо, если условие верное (True) мы передвигаем на 1 индекс вправо
#
#         while j > left and arr[j] >= pivot:    # Проверяем, больше ли индекс j, чем начало left и больше либо равно элемент j и pivot.
#             j -= 1    # И если это так, то мы передвигаем каждый раз j в левую часть массива на 1 индекс.
#
#         if i < j:    # Проверка, не пересеклись ли эти два элемента, после завершения циклов и если они НЕ пересеклись - мы реализуем обмен значений, меняем элементы местами индекса i с индексом j.
#             arr[i], arr[j] = arr[j], arr[i]
#
#     if arr[i] > pivot:    # Теперь необходимо учесть, что будет, если пересекутся i и j.
#         arr[i], arr[right] = arr[right], arr[i]    # Необходимо сделать ещё один обмен, поменять местами два элемента
#
#     return i    # Возвращаем i для рекурсивной функции quicksort, она необходима для определения где разбить массива, чтобы вызвать quicksort рекурсивно.


# def quicksort(arr, left, right):
#     if left < right:
#         pivot_pos = partition(arr, left, right)
#         quicksort(arr, left, pivot_pos - 1)
#         quicksort(arr, pivot_pos + 1, right)
#
# def partition(arr, left, right):
#     i = left    # 0
#     j = right - 1    # 6
#     pivot = arr[right]    # 44
#
#     while i < j:    # Пока индексы не пересеклись
#         while i < right and j < arr[i] < pivot:    # Пока индекс i меньше индекса правой части, или же пока i не дошёл до конца списка И элемент i меньше pivot это последни элемент
#             i += 1    # i идёт вправо увеличиваясь каждый раз на 1 индекс
#
#         while j > left and arr[j] >= pivot:
#             j -= 1    # j идёт влево уменьшаясь на 1 индекс
#
#         if i < j:    # Проверка не пересеклись ли индексы, после завершения циклов
#             arr[i], arr[j] = arr[j], arr[i]
#
#     if arr[i] > pivot:    # Далее необходимо учесть, что будет, если i и j пересекутся, к примеру, если i пройдёт за j к концу, и, j пройдёт за i в начало
#         arr[i], arr[right] = arr[right], arr[i]
#
#     return i
#
# a = [22, 11, 88, 55, 77, 66, 44]
# quicksort(a, 0, len(a) - 1)
# print(a)