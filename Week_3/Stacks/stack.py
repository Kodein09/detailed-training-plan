# stack = []
#
# #Add
# stack.append(0)
# stack.append(5)
# stack.append(10)
# stack.append(20)
#
# #Peek
# print(f"Peek: {stack[-1]}")
#
# #Pop
# print(f"Popped element: {stack.pop()}")
#
# #Stack after Pop
# print(f"Stack after pop: {stack}")
#
# #isEmpty
# print(f"isEmpty: {not bool(stack)}")
#
# #Size
# print(f"Size of the stack: {len(stack)}")
#
# #Pop
# print(f"Popped element: {stack.pop()}")
# print(f"Popped element: {stack.pop()}")
# print(f"Popped element: {stack.pop()}")
#
# #Size
# print(f"Size: {len(stack)}")
#
# #isEmpty
# print(f"Is empty: {not bool(stack)}")
from fontTools.misc.cython import returns

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, element):
#         return self.stack.append(element)
#
#     def pop(self):
#         if self.is_empty():
#             return "Stack is empty."
#         return self.stack.pop()
#
#     def peek(self):
#         if self.is_empty():
#             return "Stack is empty."
#         return self.stack[-1]
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def size(self):
#         if self.is_empty():
#             return "Stack is empty."
#         return len(self.stack)
#
# #Create a Stack
# my_Stack = Stack()
#
# #Objects
# print(f"Added: {my_Stack.push('R')}")
# print(f"Added: {my_Stack.push('o')}")
# print(f"Added: {my_Stack.push('y')}")
# print(f"Added: {my_Stack.push('_')}")
# print(f"Is empty: {my_Stack.is_empty()}")
# print(f"Size: {my_Stack.size()}")
# print(f"Peek: {my_Stack.peek()}")
# print(f"Popped element: {my_Stack.pop()}")
# print(f"Peek: {my_Stack.peek()}")
# print(f"My Stack: {str(my_Stack.stack).split()}")

# Stack структура данных, работающая по принципу LIFO (Last-in-First-out). Для примера возьму очень популярный пример, когда берут и выкладывают книги
# в одну стопку и последний элемент в этой стопке и будет самым первым на выходе.

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, element):
#         self.stack.append(element)
#         return element
#
#     def pop(self):
#         return self.stack.pop()
#
#     def last_peek(self):
#         return self.stack[-1]
#
#     def is_empty(self):
#         return not bool(self.stack)
#
# my_stack = Stack()
# pairs = {')':'(', ']':'[', '}':'{'}
# string = input("Row: ")
# for letter in string:
#     if letter == '(' or letter == '[' or letter == '{':
#         my_stack.push(letter)
#
#     if letter in pairs:
#         if my_stack.is_empty():
#             raise ValueError("Empty stack.")
#
#         if my_stack.last_peek() == pairs[letter]:
#             my_stack.pop()
#
#         else:
#             raise ValueError("another pairs.")
#
# if my_stack.is_empty():
#     print("Balanced.")
# else:
#     print("Not balanced.")

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def append(self, value):
#         self.stack.append(value)
#         return value
#
#     def pop(self):
#         return self.stack.pop()
#
#     def peek(self):
#         if self.stack:
#             return self.stack[-1]
#         return None
#
#     def size(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
# stack = Stack()
# stack.append(1)
# stack.append(3)
# stack.append(10)
# stack.append(32)
#
# print(stack.peek())
# print(stack.size())
# print(stack.pop())
#
#
# import unittest
# class TestStack(unittest.TestCase):
#     def setUp(self):
#         self.stack = Stack()
#
#     def test_append(self):
#         self.stack.append(1)
#         self.stack.append(2)
#         self.assertEqual(self.stack.peek(), 2)
#
#     def test_pop(self):
#         self.stack.append(1)
#         self.stack.pop()
#         self.assertEqual(self.stack.size(), 0)
#
#     def test_peek(self):
#         self.stack.append(1)
#         self.stack.append(95)
#         self.stack.append(100)
#         self.assertEqual(self.stack.peek(), 100)
#
#     def test_is_empty(self):
#         self.stack.append(253)
#         self.assertEqual(self.stack.is_empty(), False)
#         self.stack.pop()
#         self.assertEqual(self.stack.is_empty(), True)
#
#     def test_size(self):
#         self.stack.append(1)
#         self.stack.append(2)
#         self.stack.append(3)
#         self.stack.append(4)
#         self.assertEqual(self.stack.size(), 4)

# pairs = {')': '(', ']': '[', '}': '{'}
# def stack_pairs(s: str):
#     stack = []
#     for letter in s:
#         if letter == '(' or letter == '[' or letter == '{':
#             stack.append(letter)
#
#         if letter in pairs:
#             if stack[-1] == pairs[letter]:
#                 stack.pop()
#
#             if len(stack) == 0:
#                 return False
#
#             else:
#                 return False
#     return True
# print(stack_pairs('['))
