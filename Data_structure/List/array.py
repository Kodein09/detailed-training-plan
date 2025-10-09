# def reverse_array(a):
#     return a[::-1]
#
# nums = int(input())
# a = list(map(int, input().split()))
# print(*reverse_array(a))


def binary_search(arr, target):
    for i in range(len(arr)):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            print(f"Check index {mid}, value {arr[mid]}")

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return -1


nums = [1,2,3,4,5,6,7]
tar = 1
print(binary_search(nums, tar))