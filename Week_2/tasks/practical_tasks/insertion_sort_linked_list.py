# import unittest
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#     def from_list(self, lst):
#         if not lst:
#             return None
#
#         head = lst[0]
#         current = head
#
#         for value in lst[:1]:
#             current.next = value
#             current = current.next
#
#         return head
#
#     def to_list(self, head):
#         if not head:
#             return None
#
#         new_list = []
#         current = head
#         while current:
#             new_list.append(current)
#             current = current.next
#
#         return new_list
#
#     @staticmethod
#     def insertion_sort(arr):
#         for i in range(0, len(arr) - 1):
#             min_index = i
#             for j in range(i, 0, -1):
#                 if arr[j] < arr[min_index]:
#                     min_index = j
#                 arr[j], arr[min_index] = arr[min_index], arr[j]
#         return arr
#
# class Test(unittest.TestCase):
#     def test_linked_list(self):
#         self.assertEqual()
#
#     def test_insertion_sort(self):
#         array = [4, 3, 1, 7, 0, 9]
#         result = Node.insertion_sort(array.copy())
#         self.assertEqual(result, [0, 1, 3, 4, 7, 9])

# class InsertionSortAndLinkedList:
#     class Node:
#         def __init__(self, value):
#             self.value = value
#             self.next = None
#
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = self.Node(value)
#
#         if not self.head:
#             self.head = new_node
#             return
#
#         current = self.head
#         while current.next:
#             current = current.next
#
#         current.next = new_node
#
#     def search(self, value):
#         if not self.head:
#             return None
#         current = self.head
#         while current.next:
#             if current.value == value:
#                 return current
#             current = current.next
#         return None
#
#     def delete(self, value):
#         if not self.head:
#             return
#
#         if self.head.value == value:
#             self.head = self.head.next
#             return
#
#         prev = self.head
#         current = self.head.next
#         while current:
#             if current.value == value:
#                 prev.next = current.next
#                 current.next = None
#                 return
#             prev = current
#             current = current.next
#
#     def insertion_sort(self):
#         if not self.head or not self.head.next:
#             return
#
#         sorted_head = self.head
#         current = self.head.next
#         sorted_head.next = None
#
#         while current:
#             next_node = current.next
#
#             if sorted_head.value > current.value:
#                 current.next = sorted_head
#                 sorted_head = current
#             else:
#                 search = sorted_head
#                 while search.next and search.next.value < current.value:
#                     search = search.next
#
#                 current.next = search.next
#                 search.next = current
#
#             current = next_node
#
#         self.head = sorted_head

    # def insertion_sort(self):
    #     if not self.head:
    #         return
    #
    #     prev = self.head
    #     current = self.head.next
    #     while current:
    #         if prev.value > current.value:
    #             prev.next = current.next
    #             current.next = prev
    #         prev = current
    #         current = current.next

    # def search(self, value):
    #     if not self.head:
    #         return None
    #
    #     current = self.head
    #     while current:
    #         if current.value == value:
    #             return current
    #         else:
    #             current = current.next
    #
    #     return None

    # def delete(self, value):
    #     if not self.head:
    #         return None
    #
    #     current = self.head
    #     prev = current
    #     while current.value != value:
    #         current = current.next
    #         prev = current
    #
    #     current.next = current.next.next
    #     prev.next = current

# ll = InsertionSortAndLinkedList()
# ll.append(10)
# print(ll.head.value)
# ll.append(20)
# print(ll.head.next.value)
# ll.append(5)
# print(ll.head.next.next.value)
# print("Searching value:", ll.search(5))
# ll.insertion_sort()
# print(ll.head.value)


# class InsertionSortAndLinkedList:
#     class Node:
#         def __init__(self, value):
#             self.value = value
#             self.next = None
#
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = self.Node(value)
#         if not self.head:
#             self.head = new_node
#             return
#
#         current = self.head
#         while current.next is not None:
#             current = current.next
#
#         current.next = new_node
#
#     def search(self, value):
#         current = self.head
#         while current is not None:
#             if current.value == value:
#                 return current.value
#             else:
#                 current = current.next
#         return None
#
#     def sorted_insert(self, node, sorted_head):
#         #Случай, когда head отсутствует либо следующая нода меньше, чем текущий head
#         if not sorted_head or node.value < sorted_head.value:
#             node.next = sorted_head
#             return node
#
#         #Обход по связному списку, пока не будет найдена нода с меньшим числом, чем у переданной node в аргументе
#         current = sorted_head
#         while current.next and current.next.value < node.value:
#             current = current.next
#
#         #
#         node.next = current
#         current.next = node
#         return sorted_head
#
#     def insertion_sort(self):
#         if not self.head:
#             return None
#
#         sorted_head = None
#         current = self.head
#
#         while current:
#             next_node = current.next
#             current.next = None
#             sorted_head = self.sorted_insert(current, sorted_head)
#             current = next_node
#
#         self.head = sorted_head
#
#     @staticmethod
#     def print_list(current):
#         while current is not None:
#             print(current.value, end=' ')
#             current = current.next
#         print()
#
# ll = InsertionSortAndLinkedList()
# ll.append(5)
# ll.append(4)
# ll.append(3)
# ll.append(2)
# ll.append(1)
# result = ll.search(4)
# print("Search in linked list:", result)
# ll.insertion_sort()
# ll.print_list(ll.head)

# class LinkedListAndInsertionSort:
#     class Node:
#         def __init__(self, value):
#             self.value = value
#             self.next = None
#
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = self.Node(value)
#         if not self.head:
#             self.head = new_node
#             return
#
#         current = self.head
#         while current.next is not None:
#             current = current.next
#
#         current.next = new_node
#         return
#
#     def search(self, value):
#         current = self.head
#         while current:
#             if current.value == value:
#                 return current.value
#             else:
#                 current = current.next
#         return None
#
#     def insertion_sort(self):
#         sorted_head = None
#         current = self.head
#
#         while current:
#             sorted_head = self.sorted_list(current, sorted_head)
#
#
#     def sorted_list(self, node, sorted_head):
#         pass
#
# ll = LinkedListAndInsertionSort()
# ll.append(62)
# ll.append(23)
# ll.append(8)
# print(ll.head.value)
# print(ll.head.next.value)
# print(ll.head.next.next.value)
# print("Resul:", ll.search(8))

# class LinkedList:
#     class Node:
#         def __init__(self, value):
#             self.value = value
#             self.next = None
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def linked_list_insertion_sort(self):
#         if not self.head:
#             return None
#
#         sorted_head = None
#         current = self.head
#
#         while current:
#             next_node = current.next
#
#             if not sorted_head or current.value < sorted_head.value:
#                 current.next = sorted_head
#                 sorted_head = current
#             else:
#                 search = sorted_head
#                 while search.next and search.next.value < current.value:
#                     search = search.next
#
#                 current.next = search.next
#                 search.next = current
#
#             current = next_node
#         self.head = sorted_head
#
#         current = self.head
#         while current and current.next:
#             current = current.next
#         self.tail = current
#         return True
#
#     def add(self, value: int) -> None:
#         new_node = self.Node(value)
#
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         self.tail.next = new_node
#         self.tail = new_node
#
#     def search(self, value: int) -> str:
#         if not self.head:
#             return f"Linked list not exist"
#
#         current = self.head
#         while current is not None:
#             if current.value == value:
#                 return f"Search result: {current.value}"
#
#             current = current.next
#         return f"Not exist in Linked list"
#
#     def delete(self, value: int) -> str:
#         if not self.head:
#             return f"Linked list not exist"
#
#         if self.head.value == value:
#             self.head = self.head.next
#             if not self.head:
#                 self.tail = None
#             return f"Successfully deleted"
#
#         current = self.head
#         previous = None
#
#         while current:
#             if current.value == value:
#                 previous.next = current.next
#                 if current == self.tail:
#                     self.tail = previous
#                 return f"Successfully deleted"
#
#             previous = current
#             current = current.next
#         return "Not exist in Linked list"
#
#
# ll = LinkedList()
# ll.add(30)
# ll.add(20)
# ll.add(10)
# print(ll.head.value)
# print(ll.head.next.value)
# print(ll.head.next.next.value)
#
# print(ll.search(20))
# # print(ll.delete(30))
#
# ll.linked_list_insertion_sort()
# print(ll.head.value)
# print(ll.head.next.value)
# print(ll.head.next.next.value)


class LinkedList:
    class Node:
        def __init__(self, value: int) -> None:
            self.value = value
            self.next = None

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, value: int) -> bool:
        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return True

        self.tail.next = new_node
        self.tail = new_node
        return True

    def search(self, value: int) -> str:
        if not self.head:
            return f"Linked list not exist"

        current = self.head
        while current:
            if current.value == value:
                return f"Found value: {current.value}"
            else:
                current = current.next
        return f"Value not found"

    def delete(self, value: int) -> str:
        if not self.head:
            return f"Linked list not exist"

        if self.head.value == value:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return f"Value successfully deleted"

        current = self.head.next
        previous = self.head
        while current:
            if current.value == value:
                previous.next = current.next
                if current == self.tail:
                    self.tail = previous
                return f"Value successfully deleted"
            previous = current
            current = current.next
        return f"Value not found"

    def insertion_search(self) -> None:
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next

            if not sorted_head or current.value < sorted_head.value:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next and search.next.value < current.value:
                    search = search.next

                current.next = search.next
                search.next = current

            current = next_node

        self.head = sorted_head

        temp = self.head
        while temp.next:
            temp = temp.next
        self.tail = temp
        return