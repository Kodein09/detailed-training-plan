my_tuple = (1,2,3,4)
my_list = list(my_tuple)
my_list[3] = "five"
my_tuple = tuple(my_list)
print(my_tuple)