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