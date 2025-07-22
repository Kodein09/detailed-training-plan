def counting_comparisons(arr):
    for i in range(len(arr) - 1):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr

a = [9,3,5,2,4,1]
print(counting_comparisons(a))