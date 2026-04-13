# class Heap:
#     def __init__(self):
#         self.heap = []
#
#     def insert(self, value):
#         self.heap.append(value)
#         return self._heapify_up(len(self.heap) - 1)
#
#     def _heapify_up(self, i):
#         parent = (i - 1) // 2
#         print(heap.heap)
#         while i > 0 and self.heap[i] > self.heap[parent]:
#             self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
#             print(heap.heap)
#             i = parent
#             parent = (i - 1) // 2
#
#     def delete_max(self):
#         if self.is_empty():
#             return None
#
#         max_value = self.heap[0]
#         self.heap[0] = self.heap[-1]
#         self.heap.pop()
#         self._heapify_down(0)
#
#         return f"Deleted max value: {max_value}\nHeap after deleting: {heap.heap}"
#
#     def _heapify_down(self, index):
#         left_child_index = 2 * index + 1
#         right_child_index = 2 * index + 2
#         largest = index
#
#         if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
#             largest = left_child_index
#         if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
#             largest = right_child_index
#         if largest != index:
#             self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
#             self._heapify_down(largest)
#
#     def get_max(self):
#         if self.is_empty():
#             return None
#         return self.heap[0]
#
#     def get_last(self):
#         if self.is_empty():
#             return None
#         return self.heap[-1]
#
#     def is_empty(self):
#         return len(self.heap) == 0
#
# heap = Heap()
# heap.insert(10)
# heap.insert(20)
# heap.insert(30)
# heap.insert(100)
# print(heap.get_max())
# print(heap.get_last())
# print(heap.is_empty())
# print(heap.heap)
# print(heap.delete_max())


# class BinaryHeap:
#     def __init__(self):
#         self.heap = []
#
#     def insert(self, key):
#         self.heap.append(key)
#         self._heapify_up(len(self.heap) - 1)
#
#     def _heapify_up(self, index):

# class BinaryHeap:
#     def __init__(self):
#         self.heap = []

    # def insert(self, value):
    #     self.heap.append(value)
    #     #Max-heap
    #     def _sift_up(index):
    #         print(f"Heap right now: {self.heap}")
    #         while index > 0:
    #             parent = (index - 1) // 2
    #             left_child = parent * 2 + 1
    #             right_child = parent * 2 + 2
    #             heap = self.heap
    #             print(f"Parent: {heap[parent]}, left child: {heap[left_child]}")
    #
    #             if heap[index] <= heap[parent]:
    #                 break
    #
    #             heap[index], heap[parent] = (
    #                 heap[parent],
    #                 heap[index]
    #             )
    #
    #             index = parent

        # def _sift_up(index):
        #     while index > 0:
        #         parent = (index - 1) // 2
        #         heap = self.heap
        #
        #         if heap[index] <= heap[parent]:
        #                 break
        #
        #         heap[index], heap[parent] = (
        #             heap[parent],
        #             heap[index]
        #         )
        #         index = parent
        #
        # _sift_up(len(self.heap) - 1)

# heap = BinaryHeap()
# heap.insert(10)
# heap.insert(20)
# heap.insert(30)
# heap.insert(22)
# heap.insert(15)

# class BinaryHeap:
#     def __init__(self):
#         self.heap = []
#
#     def insert(self, value):
#         self.heap.append(value)
#         self._sift_up(len(self.heap) - 1)
#
#     def _sift_up(self, index):
#         heap = self.heap
#         while index > 0:
#             parent = (index - 1) // 2
#             if heap[index] <= heap[parent]:
#                 break
#             else:
#                 heap[parent], heap[index] = heap[index], heap[parent]
#                 index = parent
#
#     def extract_max(self):
#         if not self.heap:
#             raise IndexError("Empty Heap")
#
#         print(f"Heap: {self.heap}")
#         max_node = self.heap[0]
#         last_node = self.heap.pop()
#
#         if self.heap:
#             self.heap[0] = last_node
#             print(f"Heap: {self.heap}")
#             self._sift_down(0)
#
#         return max_node
#
#     def _sift_down(self, index):
#         heap = self.heap
#         size = len(heap)
#
#         while True:
#             parent = index
#             left = index * 2 + 1
#             right = index * 2 + 2
#
#             if left < size and heap[left] > heap[parent]:
#                 parent = left
#
#             if right < size and heap[right] > heap[parent]:
#                 parent = right
#
#             if parent == index:
#                 break
#
#             heap[index], heap[parent] = heap[parent], heap[index]
#             index = parent
#
#     def heapify(self, arr, size, i):
#         largest = i
#         left_child = i * 2 + 1
#         right_child = i * 2 + 2
#
#         if left_child < size  and arr[left_child] > arr[largest]:
#             largest = left_child
#
#         if right_child < size and arr[right_child] > arr[largest]:
#             largest = right_child
#
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             self.heapify(arr, size, largest)

# heapq = BinaryHeap()
# heapq.insert(10)
# heapq.insert(20)
# heapq.insert(30)
# heapq.insert(9)
# heapq.insert(18)
# heapq.extract_max()
# print(heapq.heap)

# class Heap:
#     def __init__(self):
#         self.heap = []
#
#     def insert(self, value):
#         self.heap.append(value)
#         self._sift_up(len(self.heap) - 1)
#
#     def _sift_up(self, index):
#         parent = (index - 1) // 2
#
#         while index > 0:
#             if self.heap[parent] > self.heap[index]:
#                 break
#             else:
#                 self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
#                 index = parent
#
#     def extract_root(self):
#         root = self.heap[0]
#         leaf = self.heap.pop()
#
#         if self.heap:
#             self.heap[0] = leaf
#             self._sift_down(0, len(self.heap))
#
#         return root
#
#     def _sift_down(self, index, size):
#         while True:
#             left_child = index * 2 + 1
#             right_child = index * 2 + 2
#             largest = index
#
#             if left_child < size and self.heap[left_child] > self.heap[largest]:
#                 largest = left_child
#
#             if right_child < size and self.heap[right_child] > self.heap[largest]:
#                 largest = right_child
#
#             if largest == index:
#                 break
#
#             self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
#             index = largest
#
# heap = Heap()
# heap.insert(50)
# heap.insert(30)
# heap.insert(40)
# heap.insert(10)
# heap.insert(20)
# heap.extract_root()

# class MaxHeap:
#     def __init__(self):
#         self.max_heap = []
#
#     def heapify(self, array):
#         self.max_heap = array
#         for i in range((len(self.max_heap) - 2) // 2, -1, -1):
#             self._sift_down(i, len(self.max_heap))
#
#     def insert(self, value):
#         self.max_heap.append(value)
#
#         self._sift_up(len(self.max_heap) - 1)
#
#     def _sift_up(self, index):
#         heap = self.max_heap
#
#         while index > 0:
#             parent = (index - 1) // 2
#
#             if heap[parent] >= heap[index]:
#                 break
#             else:
#                 heap[parent], heap[index] = heap[index], heap[parent]
#                 index = parent
#
#     def extract_root(self):
#         if not self.max_heap:
#             raise IndexError("Heap is empty")
#
#         root = self.max_heap[0]
#         last = self.max_heap.pop()
#
#         if self.max_heap:
#             self.max_heap[0] = last
#             self._sift_down(0, len(self.max_heap))
#
#         return root
#
#     def _sift_down(self, index, size):
#         heap = self.max_heap
#         while True:
#             left_child = index * 2 + 1
#             right_child = index * 2 + 2
#             largest = index
#
#             if left_child < size and heap[left_child] > heap[largest]:
#                 largest = left_child
#
#             if right_child < size and heap[right_child] > heap[largest]:
#                 largest = right_child
#
#             if largest == index:
#                 break
#
#             heap[largest], heap[index] = heap[index], heap[largest]
#             index = largest
#
# class MinHeap:
#     def __init__(self):
#         self.min_heap = []
#
#     def heapify(self, array):
#         self.min_heap = array
#         for i in range((len(self.min_heap) - 2) // 2, -1, -1):
#             self._sift_down(i, len(self.min_heap))
#
#     def insert(self, value):
#         self.min_heap.append(value)
#         self._sift_up(len(self.min_heap) - 1)
#
#     def _sift_up(self, index):
#         min_heap = self.min_heap
#
#         while index > 0:
#             parent = (index - 1) // 2
#
#             if min_heap[parent] < min_heap[index]:
#                 break
#
#             min_heap[parent], min_heap[index] = min_heap[index], min_heap[parent]
#             index = parent
#
#     def extract_root(self):
#         if not self.min_heap:
#             raise IndexError("Empty heap")
#
#         root = self.min_heap[0]
#         last = self.min_heap.pop()
#
#         if self.min_heap:
#             self.min_heap[0] = last
#             self._sift_down(0, len(self.min_heap))
#
#         return root
#
#     def _sift_down(self, index, size):
#         min_heap = self.min_heap
#         while True:
#             left = index * 2 + 1
#             right = index * 2 + 2
#             lowest = index
#
#             if left < size and min_heap[left] < min_heap[lowest]:
#                 lowest = left
#
#             if right < size and min_heap[right] < min_heap[lowest]:
#                 lowest = right
#
#             if lowest == index:
#                 break
#
#             min_heap[lowest], min_heap[index] = min_heap[index], min_heap[lowest]
#             index = lowest
#
# arr = [4,5,6,7,8,9]
# mh = MinHeap()
# mh.heapify(arr)

# class MinHeap:
#     def __init__(self):
#         self.heap = []
#
#     def left(self, i): return i * 2 + 1
#
#     def right(self, i): return i * 2 + 2
#
#     def parent(self, i): return (i - 1) // 2
#
#     def get_min(self): return self.heap[0]
#
#     def insert(self, key):
#         if len(self.heap) == 0:
#             self.heap.append(key)
#             return
#
#         self.heap.append(key)
#         i = len(self.heap) - 1
#
#         while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
#             p = self.parent(i)
#             self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
#             i = p
#         return
#
# min_heap = MinHeap()
# print(min_heap.insert(3))
# print(min_heap.insert(5))
# print(min_heap.insert(2))
# print(min_heap.insert(7))
# print(min_heap.heap)

# class MinHeap:
#     def __init__(self):
#         self.heap = []
#
#     def heapify(self, arr):
#         self.heap = arr
#         for i in range((len(arr) // 2) - 1, -1, -1):
#             self._sift_down(i)
#         return arr
#
#     def _sift_down(self, i):
#         while True:
#             left = self.left_child(i)
#             right = self.right_child(i)
#             smallest = i
#
#             if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#                 smallest = left
#
#             if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#                 smallest = right
#
#             if smallest == i:
#                 break
#
#             self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
#             i = smallest
#
#     def left_child(self, i): return i * 2 + 1
#     def right_child(self, i): return i * 2 + 2
#     def parent(self, i): return (i - 1) // 2
#
#     def insert(self, value):
#         if len(self.heap) == 0:
#             self.heap.append(value)
#             return
#
#         self.heap.append(value)
#         i = len(self.heap) - 1
#
#         while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
#             parent = self.parent(i)
#             print(self.heap)
#             self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
#             print(self.heap)
#             i = parent
#         return
#
#     def extract_min(self):
#         if not self.heap:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
#
#         print(f"Original heap before deletion: {self.heap}")
#
#         root_value = self.heap[0]
#         self.heap[0] = self.heap.pop()
#
#         i = 0
#         while True:
#             left_child = self.left_child(i)
#             right_child = self.right_child(i)
#             smallest = i
#             n = len(self.heap)
#
#             if left_child < n and left_child < right_child:
#                 smallest = left_child
#
#             if right_child < n and left_child > right_child:
#                 smallest = right_child
#
#             if smallest == i:
#                 break
#
#             self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
#             i = smallest
#
#         return root_value
#
#     def is_empty(self): return len(self.heap) == 0

        # while i < len(self.heap):
        #     print(f"Before: {self.heap}")
        #     if self.heap[self.left_child(i)] < self.heap[self.right_child(i)]:
        #         left = self.left_child(i)
        #         self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
        #         print(f"After: {self.heap}")
        #         i = left
        #         continue
        #     else:
        #         right = self.right_child(i)
        #         self.heap[right], self.heap[i], = self.heap[i], self.heap[right]
        #         print(f"After: {self.heap}")
        #         i = right
        #         continue
        # return f"Result: {self.heap}"

# min_heap = MinHeap()
# min_heap.insert(4)
# min_heap.insert(6)
# min_heap.insert(7)
# min_heap.insert(3)
# print(min_heap.heap)
# print(min_heap.is_empty())
# print(f"Extracted value from heap: {min_heap.extract_min()}")
# array = [7,9,5,8,0,3,4,]
# print(min_heap.heapify(array))