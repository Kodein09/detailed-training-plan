# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data=data)
#
#         if not self.head:
#             self.head = new_node
#             return
#
#         current = self.head
#
#         while current.next:
#             current = current.next
#
#         current.next = new_node
#
#     def display(self):
#         elements = []
#         current = self.head
#         while current:
#             elements.append(current.data)
#             current = current.next
#         print(" -> ".join(map(str, elements)))
#
# linked_list = LinkedList()
# linked_list.append(10)
# print(linked_list.display())


from typing import Any

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #insert
    def insert(self, value: Any, index: int) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        new_node = Node(value)
        current = self.head
        count = 0
        prev = None
        while count != index:
            count += 1
            prev = current
            current = current.next
        prev.next = new_node
        new_node.next = current
        return

    #delete
    def delete(self, index: int) -> None:
        if self.head.value is None:
            return

        current = self.head
        current_count = 0
        prev = None
        while current_count != index:
            current_count += 1
            prev = current
            current = current.next
        prev.next = current.next
        return

    #search
    def search(self, value: Any) -> Any:
        if self.head.value is None:
            return None

        current = self.head
        while current is not None:
            if current.value == value:
                return current.value
            else:
                current = current.next

        return None

    #reverse
    def reverse(self):
        if self.head.next is None:
            return self.head

        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            prev = current
        return self.head

    #pre-order
    def pre_order(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        return


ll = LinkedList()
ll.insert(1, 0)
ll.insert(2, 1)
ll.insert(3, 2)
ll.insert(4, 3)
# print(ll.pre_order())
ll.reverse()
ll.pre_order()