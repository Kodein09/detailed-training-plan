def search_insert_position(nums, x):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] < x:
            left = mid + 1

        elif nums[mid] > x:
            right = mid - 1

        else:
            return mid

    return left

print(search_insert_position([1,3,4,5,7], 6))