class MinHeap:
    def __init__(self):
        self.min_heap = []

    def heapify(self, array):
        self.min_heap = array
        for i in range((len(self.min_heap) - 2) // 2, -1, -1):
            self._sift_down(i, len(self.min_heap))

    def insert(self, value):
        self.min_heap.append(value)
        self._sift_up(len(self.min_heap) -1 )

    def _sift_up(self, index):
        heap = self.min_heap

        while index > 0:
            parent = (index - 1) // 2
            if heap[index] > heap[parent]:
                break
            else:
                heap[index], heap[parent] = heap[parent], heap[index]
                index = parent

    def extract(self):
        if not self.min_heap:
            raise IndexError("Empty heap")

        root = self.min_heap[0]
        last = self.min_heap.pop()

        if self.min_heap:
            self.min_heap[0] = last
            self._sift_down(0, len(self.min_heap))

        return root

    def _sift_down(self, index, size):
        heap = self.min_heap
        while True:
            left = index * 2 + 1
            right = index * 2 + 2
            lowest = index

            if left < size and heap[left] < heap[lowest]:
                lowest = left

            if right < size and heap[right] < heap[lowest]:
                lowest = right

            if index == lowest:
                break

            heap[lowest], heap[index] = heap[index], heap[lowest]
            index = lowest

class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def heapify(self, array):
        self.max_heap = array
        for i in range((len(array) - 2) // 2, -1, -1):
            self._sift_down(i, len(array))

    def insert(self, value):
        self.max_heap.append(value)
        self._sift_up(len(self.max_heap) - 1)

    def extract_max(self):
        root = self.max_heap[0]
        last = self.max_heap.pop()

        if self.max_heap:
            self.max_heap[0] = last
            self._sift_down(0, len(self.max_heap))

        return root

    def _sift_up(self, index):
        heap = self.max_heap

        while index > 0:
            parent = (index - 1) // 2

            if heap[parent] < heap[index]:
                heap[parent], heap[index] = heap[index], heap[parent]
                index = parent
            else:
                break

    def _sift_down(self, index, size):
        heap = self.max_heap
        while True:
            left = index * 2 + 1
            right = index * 2 + 2
            largest = index

            if left < size and heap[left] > heap[largest]:
                largest = left

            if right < size and heap[right] > heap[largest]:
                largest = right

            if largest == index:
                break

            heap[index], heap[largest] = heap[largest], heap[index]
            index = largest

import unittest

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.min_heap = MinHeap()

    def test_insert(self):
        self.min_heap.insert(10)
        self.min_heap.insert(30)
        self.min_heap.insert(20)
        self.min_heap.insert(40)
        self.assertEqual(self.min_heap.min_heap[0], 10)

    def test_extract(self):
        self.min_heap.insert(5)
        self.min_heap.insert(3)
        self.min_heap.insert(6)
        self.min_heap.insert(9)
        root = self.min_heap.extract()
        self.assertEqual(root, 3)
        self.assertEqual(self.min_heap.min_heap[0], 5)

    def test_heapify(self):
        for n in [8,6,3,9,7,2,5]:
            self.min_heap.insert(n)
        print(self.min_heap.min_heap)
        self.assertEqual(self.min_heap.min_heap[0], 2)

class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MaxHeap()

    def test_insert(self):
        self.heap.insert(10)
        self.heap.insert(30)
        self.heap.insert(20)
        self.heap.insert(40)
        self.assertEqual(self.heap.max_heap[0],40)

    def test_extract(self):
        for n in [10,30,20]:
            self.heap.insert(n)
        self.assertEqual(self.heap.max_heap[0], 30)
        root = self.heap.extract_max()
        self.assertEqual(root, 30)
        self.assertEqual(self.heap.max_heap[0], 20)

    def test_heapify(self):
        for n in [10,5,3,6,12,15]:
            self.heap.insert(n)
        self.assertEqual(self.heap.max_heap[0], 15)