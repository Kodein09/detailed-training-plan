# def retry(func):
#     def wrapper():
#         for i in range(3):
#             try:
#                 result = func()
#                 return result
#             except Exception as e:
#                 print(f"Attempt: {i + 1}, failed: {e}")
#         raise Exception("All attempts failed.")
#     return wrapper
#
# @retry
# def greet():
#     return "Hello decorator"
#
# print(greet())

# def retry(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except IndexError:
#             return func(*args, **kwargs)
#     return wrapper
#
# @retry
# def insertion_sort(arr):
#     for i in range(len(arr) - 1):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[min_index] > arr[j]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
# array = [7,8,3,4,2,1,5,10]
# print(insertion_sort(array))

def retry(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return func(*args, **kwargs)
    return wrapper

@retry
def arithmetic_progression(start, step, stop):
    result = start
    while result != stop:
        result += step
    return result

print(arithmetic_progression(0, 1, 10))