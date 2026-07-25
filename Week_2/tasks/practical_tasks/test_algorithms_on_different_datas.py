import random
from time import perf_counter

class SortingAlgorithms:

    #Bubble sort
    def bubble_sort(self, arr: list) -> list:
        for i in range(len(arr)):
            flag = False
            for j in range(1, len(arr)-i):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    flag = True
            if not flag:
                break
        return arr

    def selection_sort(self, arr: list) -> list:
        for i in range(len(arr)):
            cur_min = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[cur_min]:
                    cur_min = j
            arr[i], arr[cur_min] = arr[cur_min], arr[i]
        return arr

    def insertion_sort(self, arr: list) -> list:
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
        return arr

    def merge_sort(self, arr: list) -> None:
        if len(arr) > 1:
            left_arr = arr[:len(arr) // 2]
            right_arr = arr[len(arr) // 2:]

            #recusrion
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)

            #merge
            i, j, k = 0, 0, 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

    def quick_sort(self, arr: list, left, right):
        if left < right:
            partition_pos = self.partition(arr, left, right)
            self.quick_sort(arr, left, partition_pos - 1)
            self.quick_sort(arr, partition_pos + 1, right)

    @staticmethod
    def partition(arr, left, right):
        i, j = left, right - 1
        pivot = arr[right]
        while i < j:
            while i < right and arr[i] < pivot:
                i += 1
            while j > left and arr[j] >= pivot:
                j -= 1
            if i > j:
                arr[i], arr[j] = arr[j], arr[i]

        if arr[i] > pivot:
            arr[i], arr[right] = arr[right], arr[i]

        return i

    def heap_sort(self, arr):
        def _heapify(arr, n, i):
            largest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < n and arr[left] > largest:
                largest = left

            if right < n and arr[right] > largest:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]

                _heapify(arr, n, largest)

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            _heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            _heapify(arr, i, 0)

        return arr

    def radix_sort(self, arr):
        def _flatten(bucket):
            from functools import reduce
            return reduce(lambda x, y: x + y, bucket)

        def _get_num_digits(arr):
            return len(str(max(arr)))

        num_digits = _get_num_digits(arr)

        for digit in range(num_digits):
            bucket = [[] for _ in range(10)]
            for item in arr:
                num = (item // 10) ** digit % 10
                bucket[num].append(item)
            arr  = _flatten(bucket)

        return arr

    def counting_sort(self, arr: list) -> list:
        n = len(arr)
        max_value = max(arr)
        count = [0] * (max_value + 1)

        for num in arr:
            count[num] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        output = [0] * n
        for i in range(len(arr) - 1, -1, -1):
            value = arr[i]
            pos = count[value] - 1
            output[pos] = value
            count[value] -= 1
        return output

test = [random.randint(0, 100) for _ in range(10)]
original_ascending = [_ for _ in range(0, 2000, 1)]
original_descending = [_ for _ in range(2000, -1, -1)]
original_randoms = [random.randint(0, 5000) for _ in range(2000)]

sort = SortingAlgorithms()

def run_test(algorithm_name, algorithm_func) -> None:
    print(f"\n=== {algorithm_name} ===")

    arr = test.copy()
    start = perf_counter()
    algorithm_func(arr)
    end = perf_counter()
    print(f"Test: {(end - start) * 1000:.4f} ms")

    arr = original_descending.copy()
    start = perf_counter()
    algorithm_func(arr)
    end = perf_counter()
    print(f"Descending (Worst): {(end - start) * 1000:.4f} ms")

    arr = original_ascending.copy()
    start = perf_counter()
    algorithm_func(arr)
    end = perf_counter()
    print(f"Ascending (Best): {(end - start) * 1000:.4f} ms")

    arr = original_randoms.copy()
    start = perf_counter()
    algorithm_func(arr)
    end = perf_counter()
    print(f"Randoms (Average): {(end - start) * 1000:.4f} ms")

# run_test('Bubble sort', sort.bubble_sort)
# run_test('Selection sort', sort.selection_sort)
# run_test('Insertion sort', sort.insertion_sort)
# run_test('Merge sort', sort.merge_sort)
# run_test('Quicksort', sort.quick_sort)
# run_test('Counting Sort', sort.counting_sort)
# run_test('Radix sort', sort.radix_sort)
run_test('Heap sort', sort.heap_sort)


#bubble
# start = perf_counter()
# sort.bubble_sort(ascending)
# end = perf_counter()
# print(f"Bubble sort:\nResult for ascending order: {(end - start) * 1000:.2f}, ms O(n) - linear, best case")
#
# start = perf_counter()
# sort.bubble_sort(descending)
# end = perf_counter()
# print(f"Result for descending order: {(end - start) * 1000:.2f} ms, O(n^2) - quadratic, worst case")
#
# start = perf_counter()
# sort.bubble_sort(randoms)
# end = perf_counter()
# print(f"Result for random order: {(end - start) * 1000:.5f} ms, O(n^2) - quadratic, average case")


#selection
# start = perf_counter()
# print(sort.selection_sort(test))
# end = perf_counter()
# print(f"Result for ascending order: {end - start:.5f} seconds, Best case - O(n^2)")
#
# start = perf_counter()
# sort.selection_sort(descending)
# end = perf_counter()
# print(f"Result for descending order: {end - start:.5f} seconds, Worst case - O(n^2)")
#
# start = perf_counter()
# sort.selection_sort(randoms)
# end = perf_counter()
# print(f"Result for random order: {end - start:.5f} seconds, Average case, O(n^2)")


#insertion
# start = perf_counter()
# sort.insertion_sort(ascending)
# end = perf_counter()
# print(f"\nInsertion Sort:\nResult for ascending order: {end - start:.5f} seconds, Best case - O(n)")
#
# start = perf_counter()
# sort.insertion_sort(descending)
# end = perf_counter()
# print(f"Result for descending order: {end - start:.5f} seconds, Worst case - O(n^2)")
#
# start = perf_counter()
# sort.insertion_sort(randoms)
# end = perf_counter()
# print(f"Result for random order: {end - start:.5f} seconds, Average case - O(n^2)")


#merge
# start = perf_counter()
# sort.merge_sort(ascending)
# end = perf_counter()
# print(f"Result for ascending order: {end - start:.5f} seconds, Best case - O(n log(n))")
#
# start = perf_counter()
# sort.merge_sort(descending)
# end = perf_counter()
# print(f"Result for descending order: {end - start:.5f} seconds, Worst case - O(n log(n))")
#
# start = perf_counter()
# sort.merge_sort(randoms)
# end = perf_counter()
# print(f"Result for random order: {end - start:.5f} seconds, Average case - O(n log(n))")