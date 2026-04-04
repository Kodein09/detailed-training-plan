# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# n1 = Node(3)
# n2 = Node(0)
# n3 = Node(1)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(1)
# n7 = Node(9)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
#
# head = n1
#
# current = head
# while current:
#     print(current.value)
#     current = current.next
from Week_1.Practical_tasks.decorator_retry import retry


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# def from_list(lst):
#     if not lst:
#         return None
#
#     head = Node(lst[0])
#     current = head
#
#     for value in lst[1:]:
#         current.next = Node(value)
#         current = current.next
#
#     return head
#
# def to_list(head):
#     if not head:
#         return None
#
#     new_list = []
#     current = head
#     while current:
#         new_list.append(current.value)
#         current = current.next
#     return new_list
#
# head = from_list([3, 0, 1, 4, 5, 1, 9])
# print(to_list(head))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def insert(head, new_node, position):
#         if position == 1:
#             new_node.next = head
#             return new_node
#
#         current_node = head
#         for _ in range(position - 2):
#             if current_node is None:
#                 break
#             current_node = current_node.next
#
#         new_node.next = current_node.next
#         current_node.next = new_node
#         return head
#
#     def delete(self):
#         pass
#
#     def search(head):
#         current_node = head
#         min_value = head.data
#         while current_node:
#             if current_node.data < min_value:
#                 min_value = current_node.data
#         return min_value
#
#
#     def reverse(self):
#         pass

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     class Node:
#         def __init__(self, element, next_node=None):
#             self.element = element
#             self.next = next_node
#
#     def append(self, element):
#         if not self.head:
#             self.head = self.Node(element)
#             self.length += 1
#             return element
#
#         node = self.head
#         while node.next_node:
#             node = node.next_node
#
#         node.next_node = self.Node(element)
#         self.length += 1
#         return element
#
#     def __str__(self):
#         return
#
# a = LinkedList()
# a.append(9)

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
#
#     def push_front(self, value):
#         new_node = Node(value)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#         self.length += 1
#
#     def push_back(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#
#             while current.next:
#                 current = current.next
#             current.next = new_node
#         self.length += 1

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def  push_front(self, value):
#         new_node = Node(value)
#         if self.head:
#             new_node.next = self.head
#         else:
#             self.tail = new_node
#         self.head = new_node
#         self.length += 1
#
#     def push_back(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#
#     def insert(self, index, value):
#         if index < 0 or self.length < index:
#             raise IndexError("Index out of range")
#
#         new = Node(value)
#         if index == 0:
#             new.next = self.head
#             self.head = new
#             if self.length == 0:
#                 self.tail = new
#         else:
#             current = self.head
#             for _ in range(index - 1):
#                 current = current.next
#
#             new.next = current.next
#             current.next = new
#
#         self.length += 1
#
#     def delete_first(self):
#         if self.length == 0:
#             raise IndexError("Linked list is empty")
#         elif self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#         self.length -= 1
#
#     def delete_last(self):
#         if self.length == 0:
#             raise IndexError("Linked list is empty")
#         elif self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             current = self.head
#             while current.next is not self.tail:
#                 current = current.next
#             current.next = None
#             self.tail = current
#         self.length -= 1
#
#     def search(self, value):
#         if self.length == 0:
#             return None
#         elif self.length == 1:
#             return self.head
#         else:
#             current = self.head
#             while current:
#                 if current.data == value:
#                     return current
#                 current = current.next
#         return None
#
#     def reverse(self):
#         prev = None
#         current = self.head
#
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#
#         self.tail = self.head
#         self.head = prev

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def traversal(self, head):
#         if not self.head:
#             self.head = head
#
#         current_node = head
#         while current_node:
#             print(f"{current_node.data}", end=' -> ')
#             current_node = current_node.next
#
#         return current_node
#
#     def insert(self, new_node):
#         if not self.head:
#             self.head = new_node
#             return
#
#         new_node.next = self.head.next
#         self.head.next = new_node
#
#     def append(self, new_node):
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         self.tail.next = new_node
#         self.tail = new_node
#
#     def delete(self, data):
#         if not self.head:
#             raise ValueError("Cannot delete from empty linked list.")
#
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#
#         if self.tail.data == data:
#             current = self.head
#             while current.next is not self.tail:
#                 current = current.next
#             self.tail = current
#             self.tail.next = None
#             return
#
#         prev = None
#         current = self.head
#
#         while current:
#             if current.data == data:
#                 prev.next = current.next
#                 return
#
#             prev = current
#             current = current.next
#         raise ValueError("Value not found in the linked list")
#
#     def search(self, data):
#         if not self.head:
#             raise ValueError("Empty linked list.")
#
#         current = self.head
#         while current:
#             if current.data == data:
#                 return current
#             current = current.next
#         return None

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def merge_two_lists(self, list1, list2):
#         list1 = self.head
#         list2 = self.head
#         current = self.head
#         new_linked_list = []
#         while current:
#             if list1.data <= list2.data:
#                 new_linked_list = list2.next
#             else:
#                 new_linked_list = list1.next

# class LinkedList:
#     def __init__(self):
#         self.head = None

    # def remove_duplicates(self):
    #     if not self.head:
    #         raise ValueError("Empty linked list")
    #
    #     current = self.head
    #     while current:
    #         if current.next and current.data == current.next.data:
    #             current.next = current.next.next
    #         else:
    #             current = current.next

    # def remove_duplicates_two(self):
    #     dummy = Node(0)
    #     dummy.next = self.head
    #     current = self.head
    #     prev = dummy
    #
    #     while current:
    #         if current and current.next:
    #             while current.data == current.next.data:
    #                 current = current.next
    #             prev.next = current.next
    #         else:
    #             prev = prev.next
    #         current = current.next

    # def remove_element(self, value):
    #     if not self.head:
    #         return self.head
    #
    #     dummy = Node(0)
    #     dummy.next = self.head
    #     current = self.head
    #     prev = dummy
    #
    #     while current and current.next:
    #         if current.next and current.next.data == value:
    #             while current.next and current.next.data == value:
    #                 current = current.next
    #             prev.next = current.next
    #         else:
    #             prev = prev.next
    #         current = current.next
    #
    #     return dummy.next

# def missing_number(nums):
#         r = [x for x in range(0, len(nums) + 1)]
#
#         miss_num = 0
#         for i in range(len(nums) + 1):
#             if r[i] in nums:
#                 continue
#             else:
#                 miss_num = r[i]
#
#         return miss_num
#
# print(missing_number([0,1]))


# def single_number(nums):
#     unique_num = 0
#
#     for i in range(len(nums)):
#         unique_num = unique_num ^ nums[i]
#
#     return unique_num
#
# print(single_number([2,2,3,2]))

# def intersection_of_two_arrays(nums1: list[int], nums2: list[int]):
#     intersection = set(nums1) & set(nums2)
#     return list(intersection)
# print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n1.prev = None
# n1.next = n2
# n2.prev = n1
# n2.next = n3
# n3.prev = n2
# n3.next = None
#
# current = n1
# while current:
#     print(current.data)
#     current = current.next
#
# n1.next = n3
# n3.prev = n1
#
# current = n1
# while current:
#     print(current.data)
#     current = current.next

# new_node = Node(15)
# n1.next = new_node
# new_node.next = n2
# print()
# current = n1
# while current:
#     print(current.data)
#     current = current.next