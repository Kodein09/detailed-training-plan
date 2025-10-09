#1
# for i in range(1, 11):
#     print(i, end=' ')

#2
# for i in range(1, 11):
#     i *= 2
#     print(i, end=' ')

#3
# for i in range(1, 11):
#     i *= 5
#     print(i, end=' ')

#4
# count_sum = 0
# for i in range(1, 101):
#     count_sum += i
# print(count_sum)

#5
# for i in range(1, 11):
#     i *= i
#     print(i)

#6
# even_sum = 0
# for i in range(0, 51):
#     if i % 2 == 0:
#         even_sum += i
# print(even_sum)

#7
# odd_sum = 0
# for i in range(0, 51):
#     if i % 2 == 1:
#         odd_sum += i
# print(odd_sum)

#8
# for i in range(10, -1, -1):
#     print(i, end=' ')

#9
# my_str = 'Python'
# for letter in my_str:
#     print(letter)

#10
# vowels = ['a', 'i', 'u', 'e', 'o', 'y']
# my_string = "hello world"
# vowel_count = 0
# for letter in my_string:
#     if letter in vowels:
#         vowel_count += 1
# print(vowel_count)

#11
# count_sum = 0
# for i in range(0, 100):
#     count_sum += i
# print(count_sum)

#12
# factorial = 5
# factorial_number = 1
# for i in range(1, factorial+1):
#     factorial_number = factorial_number * i
# print(factorial_number)

#13
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f'{i}: simple')
#     else:
#         print(f'{i}: complex')

#14
# dividend = 12
# for i in range(1, dividend+1):
#     if dividend % i == 0:
#         print(i)

#15
# for i in range(1, 11):
#     for j in range(11):
#         print(i * j, end=' ')
#     print()

#16
# digit = 12345678
# count_digits = 0
# for i in str(digit):
#     if i:
#         count_digits += 1
# print(int(count_digits))

#17
# number = 709
# sum_number = 0
# for i in str(number):
#     sum_number = sum_number + int(i)
# print(sum_number)

#18
# def reversed_number(number: int):
#     num_str = str(abs(number))
#     reversed_str = ""
#
#     for i in range(len(num_str) - 1, -1, -1):
#         reversed_str += num_str[i]
#
#     reversed_num = int(reversed_str)
#
#     if number < 0:
#         return -reversed_num
#     else:
#         return reversed_num
#
# print(reversed_number(-123))

# def reversed_number(number):
#     num_str = str(abs(number))
#
#     reversed_num = str((num_str[::-1]))
#
#     if number < 0:
#         return reversed_num + '-'
#     else:
#         return str(reversed_num)
# print(reversed_number(-1200))



