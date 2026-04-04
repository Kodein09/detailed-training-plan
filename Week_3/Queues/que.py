# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, element):
#         return self.queue.append(element)
#
#     def peek(self):
#         if self.is_empty():
#             return "Queue is empty."
#         return self.queue[0]
#
#     def dequeue(self):
#         if self.is_empty():
#             return "Queue is empty."
#         return self.queue.pop()
#
#     def is_empty(self):
#         return not bool(self.queue)
#
#     def size(self):
#         return len(self.queue)
#
# my_Queue = Queue()
#
# print(f"Added: {my_Queue.enqueue(5)}")
# print(f"Added: {my_Queue.enqueue(2)}")
# print(f"Added: {my_Queue.enqueue(10)}")
# print(f"Peek: {my_Queue.peek()}")
# print(f"Size: {my_Queue.size()}")
# print(f"Is empty: {my_Queue.is_empty()}")

# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, value):
#         return self.queue.append(value)
#
#     def empty(self):
#         if self.queue:
#             return self.queue
#         return None
#
#     def dequeue(self):
#         if not self.empty():
#             return self.queue.pop(0)
#         return None
#
#     def size(self):
#         return len(self.queue)
#
#     def peek(self):
#         if not self.empty():
#             return self.queue[0]
#         return None
#
# q = Queue()
# q.queue.append(99)
# q.queue.append(104)
# q.queue.append(29)
# print(q.peek())
# print(q.size())
# print(q.empty())

#Это дорогая операция по причине того, что при удалении начального элемента все элементы в массиве сдвигаются и это занимает O(n) времени, но есть
# collections.deque благодаря этому модулю операция будет за асимптотическую временную сложность O(1) константное время.

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)
        return value

    def dequeue(self):
        if not self.empty():
            return self.queue.popleft()  #O(1)
        return None

    def peek(self):
        if not self.empty():
            return self.queue[0]
        return None

    def size(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0

que = Queue()


import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.enqueue(10), 10)

    def test_dequeue(self):
        self.queue.dequeue()
        self.assertEqual(self.queue.dequeue(), None)

    def test_peek(self):
        self.queue.enqueue(100)
        self.queue.enqueue(600)
        self.queue.enqueue(400)
        self.assertEqual(self.queue.peek(), 100)

    def test_is_empty(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.empty(), False)
        self.queue.dequeue()
        self.assertEqual(self.queue.empty(), True)

    def test_size(self):
        self.queue.enqueue(123)
        self.queue.enqueue(456)
        self.queue.enqueue(789)
        self.assertEqual(self.queue.size(), 3)