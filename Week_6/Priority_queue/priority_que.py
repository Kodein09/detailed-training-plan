#Структура данных, которая является очередью, но с одним отличием - элемент, который имеет наибольший приоритет,извлекается первым.
#Есть несколько вариантов реализации приоритетной очереди:
#1. List/Array + sort
#2. Binary heap (standard and most popular)
#min-heap - root is min element
#max-heap - root is max element
#Свойство кучи: каждая нода <= всех своих детей в случае с min-heap, max-heap - каждая нода >= всех своих детей
#Визуально это дерево, но хранится в массиве для эффективности

#У приоритетной очереди есть основные операции:
#Insert (enqueue) - вставляется элемент в конец массив и по его приоритетности дальше поднимаем до нужного места. Его сложность O(log n) для кучи
#Peek / Top - посмотреть элемент с наивысшим приоритетом, это корень кучи - O(1)
#Pop (dequeue) - извлечь элемент из массива с наивысшим приоритетом. Извлекаем корень и последним элемент ставим на место корня, затем heapify
#Change priority/ Update - редко используется, это изменяет приоритет элемента, при поддержке индекса O(log n)

# class PriorityQueue:
#     def __init__(self):
#         self.queue = []
#
#     def insert(self, value):
#         self.queue.append(value)
#
#     def pop(self) -> int:
#         try:
#             m = 0
#             for i in range(len(self.queue)):
#                 if self.queue[i] > self.queue[m]:
#                     m = i
#             item = self.queue[m]
#             del self.queue[m]
#             return item
#         except IndexError:
#             raise IndexError("Queue empty")
#
#     def is_empty(self) -> bool:
#         return len(self.queue) == 0

# class PriorityQueue:
#     def __init__(self):
#         self.queue = []
#
#     def insert(self, value):
#         self.queue.append(value)
#
#     def pop(self) -> int:
#         if not self.queue:
#             raise IndexError("Empty queue")
#
#         max_index = 0
#         for i in range(1, len(self.queue)):
#             if self.queue[i] > self.queue[max_index]:
#                 max_index = i
#
#         return self.queue.pop(max_index)
#
#     def is_empty(self) -> bool:
#         return len(self.queue) == 0

# class PriorityQueue:
#     def __init__(self):
#         self.queue = []
#
#     def insert(self, value):
#         print(f"Queue: {self.queue}")
#         i = 0
#         while i < len(self.queue) and self.queue[i] > value:
#             print(f"Comparing between: {self.queue[i]} and value: {value}")
#             i += 1
#         self.queue.insert(i, value)
#         print(f"Queue after inserting: {self.queue}")
#
#     def pop(self):
#         if not self.queue:
#             raise IndexError("Priority Queue is Empty")
#         return f"Queue now: {self.queue}\nPopped element: {self.queue.pop(0)}\nQueue after pop: {self.queue}"
#
#     def peek(self):
#         if not self.queue:
#             raise IndexError("Priority Queue is Empty")
#         return self.queue[0]
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
# pq = PriorityQueue()
# pq.insert(40)
# pq.insert(10)
# pq.insert(25)
# pq.insert(35)
# print(pq.pop())

# class PriorityQueue:
#     def __init__(self):
#         self.queue = []
#
#     def insert(self, value):
#         index = 0
#         while index < len(self.queue) and self.queue[index] > value:
#             index += 1
#         self.queue.insert(index, value)
#
#     def pop(self):
#         if not self.queue:
#             raise IndexError("Empty queue")
#         return self.queue.pop(0)
#
#     def is_empty(self):
#         return len(self.queue) == 0

    # def search(self, value):
    #     index = len(self.queue) - 1
    #     while index:
    #         if value == self.queue[index]:
    #             return self.queue[index]
    #         else:
    #             index -= 1
    #
    #     return None

#     def search(self, value):
#         for i in range(len(self.queue)):
#             if self.queue[i] == value:
#                 return self.queue[i]
#         return None
#
# pq = PriorityQueue()
# pq.insert(10)
# pq.insert(30)
# pq.insert(20)
# pq.insert(50)
# print(pq.search(10))

# class PriorityQueue:
#     def __init__(self):
#         self.queue = []
#
#     def insert(self, value):
#         index = 0
#         print(self.queue)
#         while index < len(self.queue) and self.queue[index] <= value:
#             index += 1
#         self.queue.insert(index, value)
#         print(self.queue)
#
#     def pop(self):
#         if not self.queue:
#             raise IndexError("Empty queue")
#         return self.queue.pop(0)
#
# que = PriorityQueue()
# que.insert(10)
# que.insert(15)
# que.insert(5)

class PriorityQueue:
    def __init__(self, items=None, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap
        if items:
            self.heap = list(items)
            self._build_heap()

    def _comparison(self, value1, value2):
        if self.is_min_heap:
            return value1 < value2
        return value1 > value2

    def _shift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] > self.heap[i]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _shift_down(self, i):
        self.heap[0] = self.heap.pop()

        while i < len(self.heap):
            left = i * 2 + 1
            right = i * 2 + 2
            root = 0

            if left < len(self.heap) and self._comparison(self.heap[left], self.heap[root]):
                root = left

            if right < len(self.heap) and self._comparison(self.heap[right], self.heap[root]):
                root = right

            if root == i:
                break

            self.heap[i], self.heap[root] = self.heap[root], self.heap[i]
            i = root

    def _build_heap(self):
        for i in range((len(self.heap) - 1), -1, -1):
            self._shift_down(i)

    def push(self, value):
        self.heap.append(value)
        self._shift_up(len(self.heap) - 1)

    def pop(self):
        root = self.heap[0]
        self._shift_down(0)
        return root