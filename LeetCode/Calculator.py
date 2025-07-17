# class Calculator:
#     @staticmethod
#     def calculate():
#         try:
#             while True:
#                 num1 = float(input("Enter first integer: "))
#                 operation = input("Choose the one operation: (+, -, /, *): ")
#                 num2 = float(input("Enter second integer: "))
#
#                 if operation == "+":
#                     result = num1 + num2
#                 elif operation == "-":
#                     result = num1 - num2
#                 elif operation == "/":
#                     if num2 == 0:
#                         raise ValueError("Can't divide to zero!")
#                     result = num1 / num2
#                 elif operation == "*":
#                     result = num1 * num2
#                 else:
#                     raise ValueError("Incorrect operation!")
#
#                 print(f"Result: {result}")
#
#         except Exception as e:
#             print(f"Error: {repr(e)}")
#
# Calculator.calculate()