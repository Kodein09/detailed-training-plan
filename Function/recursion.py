# def recursive(func):
#     print(func)
#     recursive(func + 1)
# print(recursive(0))

# В Python существует стек вызова функций, для того, чтобы функция имела порядок вызова другой функции откуда, какая и где была вызвана.
# Каждый раз стек вызова функций принимает в себя функцию, но он не бесконечный и имеет ограничение, на 997 итерации произойдёт переполнение данного стека.
# Можно ограничить глубину рекурсии, дабы избежать переполнения и ошибки рекурсии, это реализуется через какое-либо условие остановки\выхода из функций
#Пример:
# def recursion(f):
#     if f < 4:
#         print(f)
#         return recursion(f+1)
#     else:
#         return "Condition was complete."
# print(recursion(1))

#Есть ещё один пример, в нём наглядно показано, как ведут себя рекурсивные циклы после их завершения:
# def recursive(arg):
#     if arg < 4:
#         print(arg)
#         recursive(arg + 1)
#     print(arg)
# print(recursive(1))
#Видно, как стек рекурсии возвращается к прошлой функции, которая не до конца завершила свою работу, после чего завершает и снова возвращается к предыдущей функции.

#Factorial
# def factorial(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

#Обход корня или каталогов
# F = {
#     "C:": {
#         "Python/": ["readme.md", "__init__.py", "recursion.py"],
#         "Projects/": {
#             "Todo/": ["readme.md", 'temp.html', 'script.js'],
#             "Fastapi/": ["docker", ".gitignore", "main.py"]
#         },
#         "Windows/": {
#             "System32/": ["acledit.dll", "aclui.dll", "zipfldr.dll"]
#         }
#     }
# }
#
# def traversal_tree(path, depth=0):
#     for f in path:
#         print(" " * depth, f)
#         if type(path[f]) == dict:
#             traversal_tree(path[f], depth + 1)
#         else:
#             print(" " * (depth + 1), " ".join(path[f]))
# print(traversal_tree(F, 0))

#count elements
# def count_elements(lst):
#     if not lst:
#         return 0
#     else:
#         head, *tail = lst
#         print(head)
#         print(tail)
#         return 1 + count_elements(tail)
# print(count_elements([1,6,4,8,5,9,546,986]))