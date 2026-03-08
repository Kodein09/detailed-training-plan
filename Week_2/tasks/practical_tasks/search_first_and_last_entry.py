def binary_search_first_entry(arr, search_item):
    low = 0
    high = len(arr) - 1 
    result = -1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]

        if guess == search_item:
            result = middle
            high = middle - 1

        elif guess < search_item:
            low = middle + 1
        else:
            high = middle - 1
    return result
print(binary_search_first_entry([1,2,3,4,5,6,7,8,9,9,9,9,9,10,11,12,13,14,15], 9))

def binary_search_last_entry(arr, search_item):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]

        if guess == search_item:
            result = middle
            low = middle + 1

        elif guess < search_item:
            low = middle + 1

        else:
            high = middle - 1

    return result
print(binary_search_last_entry([0,1,10,10,10,10], 10))