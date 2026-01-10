# def reading_file(file, chunk_size = 512):
#     with open(file, "r") as f:
#         while True:
#             chunk = f.read(chunk_size)
#             if not chunk:
#                 break
#             else:
#                 yield chunk
#
# import time
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         print(f"Func {func.__name__} runtime: {elapsed_time:.6f} seconds")
#         return result
#     return wrapper

# from time import time
#
# def execution_time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         return f"Result of func: {result}\n:Execution time: {end - start}"
#     return wrapper
#
# @execution_time
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# print(bubble_sort([6,5,3,1,2]))

