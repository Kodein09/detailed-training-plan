#First: Squares
nums = [0,1,2,3,4,5,6,7,8,9,10]
squares = [x ** 2 for x in nums]
print(squares)

#Second: Even
even = [x for x in range(0, 21) if x % 2 == 0]
print(even)

#Third: Filtering strings
words = ["hello", "ok", "sun", "go", "goodbye"]
new_list = [i for i in words if len(i) > 2]
print(new_list)

#Fouth: Multiply
nums = [1,2,3,4]
multiple = [i * 2 for i in nums]
print(multiple)

#Fifth: Words len
fruits = ["apple", "banana", "kiwi"]
len_words = [len(fruit) for fruit in fruits]
print(len_words)

#Sixth: upper()
words = ["hi", "hello", "hey"]
upper_version_1 = [i.upper() for i in words]
upper_version_2 = [i.swapcase() for i in words]
print(upper_version_1, upper_version_2)

#Seventh: isalnum()
text = 'a1b2c3d4'
only_numbers = [i for i in text if i.isdigit()]
print(*only_numbers)

#Eighth: Multiples
multiples = [i for i in range(1, 51) if i % 3 == 0 or i % 5 == 0]
print(multiples)

#Ninth: Even squares
even_squares = [i ** 2 for i in range(1, 21) if i % 2 == 0]
print(even_squares)

#Tenth: Matrix rotation
matrix = [[1,2,3],[4,5,6]]
rotation = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(rotation)