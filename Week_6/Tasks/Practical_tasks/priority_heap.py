#from collections import deque

# class PriorityHeap:
#     def __init__(self):
#         self.priority_queue = deque()
#
#     def insert(self, value):
#         index = 0
#         print(self.priority_queue)
#         while index < len(self.priority_queue) and self.priority_queue[index] <= value:
#             index += 1
#         self.priority_queue.insert(index, value)
#         print(self.priority_queue)
#
#     def pop(self):
#         if not self.priority_queue:
#             raise IndexError("Empty que")
#         return self.priority_queue.popleft()
#
#     def heapify(self, array):
#         self.priority_queue = array
#         for i in range((len(self.priority_queue) - 2) // 2, -1, -1):
#             self._sift_down(0, len(self.priority_queue))
#
#     def _sift_down(self, index, size):
#         que = self.priority_queue
#
#         while True:
#             left = index * 2 + 1
#             right = index * 2 + 2
#             lowest = index
#
#             if left < size and que[lowest] > que[left]:
#                 lowest = left
#
#             if right < size and que[lowest] > que[right]:
#                 lowest = right
#
#             if lowest == index:
#                 break
#
#             que[lowest], que[index] = que[index], que[lowest]
#             index = lowest

class PriorityHeap:
    def __init__(self):
        self.priority_heap = []

    def insert(self, value):
        self.priority_heap.append(value)
        self._sift_up(len(self.priority_heap) - 1)

    def extract(self):
        if not self.priority_heap:
            raise IndexError("Empty priority heap")

        root = self.priority_heap[0]
        last = self.priority_heap.pop()

        if self.priority_heap:
            self.priority_heap[0] = last
            self._sift_down(0, len(self.priority_heap))

        return root

    def heapify(self, array):
        self.priority_heap = array
        for i in range((len(self.priority_heap) - 2) // 2, -1, -1):
            self._sift_down(i, len(self.priority_heap))

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.priority_heap[index] < self.priority_heap[parent]:
                self.priority_heap[index], self.priority_heap[parent] = self.priority_heap[parent], self.priority_heap[index]
            else:
                break

    def _sift_down(self, index, size):
        while True:
            left = index * 2 + 1
            right = index * 2 + 2
            lowest = index

            if left < size and self.priority_heap[left] < self.priority_heap[lowest]:
                lowest = left

            if right < size and self.priority_heap[right] < self.priority_heap[lowest]:
                lowest = right

            if lowest == index:
                break

            self.priority_heap[lowest], self.priority_heap[index] = self.priority_heap[index], self.priority_heap[lowest]
            index = lowest

import unittest

class TestPriorityHeap(unittest.TestCase):
    def setUp(self):
        self.heap = PriorityHeap()

    def test_insert(self):
        for n in [20, 15, 25]:
            self.heap.insert(n)
        self.assertEqual(self.heap.priority_heap[0], 15)

    def test_extract(self):
        for n in [5,2,6,3]:
            self.heap.insert(n)
        root = self.heap.extract()
        self.assertEqual(root, 2)

    def test_heapify(self):
        for n in [10,5,15]:
            self.heap.insert(n)
        self.assertEqual(self.heap.priority_heap[0], 5)