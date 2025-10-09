# my_tuple = (1,2,3,4) #unmutable
# my_list = [1,2,3,4] #mutable
#
# duplicate_tuple = (1,1,2,3,3,4,5,4,6) # Allow duplicates
#
# not_a_tuple = ("string") # str <class 'str'>
# print(type(not_a_tuple))
# a_tuple = ("tuple",) #tuple <class 'tuple'>
# print(type(a_tuple))
#
#


t = ('a', 'b', 'c')
t2 = (1,2,3,3,3,3,3,3)
t3 = t + t2
print(t3)
print(t3.count(3))    # Count values in tuple
print(t3.index('c'))    # Return index of a value