from collections import deque
#
# a = deque([1,2,3], maxlen=3)
# a.append(4)
# print(a)
# a.appendleft(5)
# print(a)
#
# #1
# queue = deque([1,2,3,4,5], maxlen=5)
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# queue.append(50)
# queue.append(60)
# queue.append(70)
# print(queue)
#
# #2
# q = deque([10,15,20], maxlen=3)
# q.appendleft(1)
# q.appendleft(2)
# q.appendleft(3)
# q.appendleft(4)
# print(q)
#
# #3
# simulation = deque(["hello", "world"], maxlen=5)
# simulation.append('open')
# simulation.append('edit')
# simulation.append('save')
# last = simulation.pop()
# print(last)
#
# #4
# def is_palindrome(s: str) -> bool:
#     text = deque(char.lower() for char in s if char.isalnum())
#     while len(text) > 1:
#         if text.popleft()!= text.pop():
#             return False
#     return True


# def is_palindrome(text: str) -> bool:
#     text = deque(char.lower() for char in text if char.isalnum())
#     while len(text) > 1:
#         if text.popleft() != text.pop():
#             return False
#     return True
#
# print(is_palindrome("deed"))
# print(is_palindrome("peep"))
# print(is_palindrome("hello"))

#
# #5
# nums = deque([1,2,3])
# nums.append(4)
# nums.append(5)
# nums.appendleft(0)
# print(nums)
#
# #5: version 2
# nums = deque([1,2,3])
# nums.extendleft([0])
# nums.extend([4,5])
# print(nums)
#
# #6
# def track_last(n):
#     que = deque(maxlen=n)
#     for i in range(10):
#         que.append(f"event_{i}")
#     return que
#
# print(track_last(5))


# def is_palindrome(num: int) -> bool:
#     digit = deque(str(num))
#     while len(digit) > 1:
#         if digit.popleft() != digit.pop():
#             return False
#     return True
#
# print(is_palindrome(7))
# print(is_palindrome(121))
# print(is_palindrome(111))
# print(is_palindrome(113))

# l = [1,2,3,4]
# l2 = [5,6,7,8]
# l.extend(l2)
# print(l)
# from collections import deque
# l3 = deque(l)
# l3.appendleft(0)
# print(l3)
# l3.remove(4)
# print(l3)
# l3.pop()
# print(l3)
# l3.popleft()
# print(l3)
# print(l3.index(7))
# print(l3.index(7, 0, 6))
# l3.reverse()
# print(l3)
# l3.insert(0, 3)
# l3.insert(0, 3)
# l3.insert(0, 3)
# print(l3)
# print(l3.count(3))
# l3.reverse()
# l3.insert(3, 4)
# l3.insert(0, 0)
# print(l3)
# l4 = l3.copy()
# print(l4)
# print(l3)
# l4.pop()
# l4.pop()
# l4.pop()
# print(l4)
# l3.clear()
# l4.clear()
# print(l3, l4)