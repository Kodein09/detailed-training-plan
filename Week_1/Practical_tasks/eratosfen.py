# def prime_generator(n):
#     is_prime = [True] * n
#     n = len(is_prime)
#     for i in range(2, int(n**0.5) + 1):
#         for j in range(i*i, n, i):
#             is_prime[j] = False
#     for i in range(2, n):
#         if is_prime[i]:
#             yield i
#
# print(*prime_generator(30))


# def prime_gen(n):
#     is_prime = [True] * n
#     for i in range(2, int(n**0.5)+1):
#         for j in range(i * i, n, i):
#             is_prime[j] = False
#
#     for i in range(2, n):
#         if is_prime[i]:
#             yield i
#
# print(*prime_gen(10))

# def prime_gen(x):
#     is_prime = [True] * x
#     for i in range(2, int(x**0.5)+1):
#         for j in range(i * i, x, i):
#             is_prime[j] = False
#
#     for i in range(2, x):
#         if is_prime[i]:
#             yield i
# print(*prime_gen(10))