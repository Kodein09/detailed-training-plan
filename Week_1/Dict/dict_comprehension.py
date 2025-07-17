dict_comprehension = {key: value for (key,value) in zip([1,2,3], ['a', 'b', 'c'])}
print(dict_comprehension)

vector = [[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12], [13,14,15], [16,17,18]]]
inline = [
    digit
    for i in vector
    for j in i
    for digit in j
          ]
print(inline)