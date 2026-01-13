def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

        else:
            return mid
    return -1

print(binary_search([-1,0,2,3,5,7], 7))