# def reversed_integer(x: int) -> int:
#     reversed_int = 0
#     if x < 0:
#         y = -x
#         while y > 0:
#             reversed_int = reversed_int * 10 + (y % 10)
#             y //= 10
#         return -reversed_int
#     else:
#         while x > 0:
#             reversed_int = reversed_int * 10 + (x % 10)
#             x //= 10
#         return reversed_int
# print(reversed_integer(123))

# def reversed_int(n: int) -> bool:
#     palindrome = n
#     rev = 0
#     while n > 0:
#         rev = rev * 10 + (n % 10)
#         n //= 10
#         if rev == palindrome:
#             return True
#     else:
#         return False
# print(reversed_int(1))

def is_palindrome(x: int) -> bool:
    palindrome = x
    rev = 0
    if x == 0:
        return True
    while x > 0 :
        rev = rev * 10 + (x % 10)
        x //= 10
        if rev == palindrome:
            return True
    return False
print(is_palindrome(121))