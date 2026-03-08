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
        print(f"Просеивание вниз: {arr}, поменял местами элементы {arr[largest]} и {arr[root_index]}")
        heapify(arr, heap_size, largest)

def heap_sort(arr):
    #В этом цикле происходит построение кучи
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)
        print(f"Построение кучи: {arr}")

    # В этом цикле происходит сортировка
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Обмен корня с элементом: {arr}")
        heapify(arr, i, 0)

    return arr

array = [10, 40, 50, 30, 20]
print(heap_sort(array))