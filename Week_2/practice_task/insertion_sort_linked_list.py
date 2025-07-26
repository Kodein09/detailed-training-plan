import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def from_list(self, lst):
        if not lst:
            return None

        head = lst[0]
        current = head

        for value in lst[:1]:
            current.next = value
            current = current.next

        return head

    def to_list(self, head):
        if not head:
            return None

        new_list = []
        current = head
        while current:
            new_list.append(current)
            current = current.next

        return new_list

    @staticmethod
    def insertion_sort(arr):
        for i in range(0, len(arr) - 1):
            min_index = i
            for j in range(i, 0, -1):
                if arr[j] < arr[min_index]:
                    min_index = j
                arr[j], arr[min_index] = arr[min_index], arr[j]
        return arr

class Test(unittest.TestCase):
    def test_linked_list(self):
        self.assertEqual()

    def test_insertion_sort(self):
        array = [4, 3, 1, 7, 0, 9]
        result = Node.insertion_sort(array.copy())
        self.assertEqual(result, [0, 1, 3, 4, 7, 9])