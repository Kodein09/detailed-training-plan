# def selection_sort(bucket):
#     for i in range(len(bucket) - 1):
#         key = i
#         for j in range(i + 1, len(bucket)):
#             if bucket[j] < bucket[key]:
#                 key = j
#         bucket[i], bucket[key] = bucket[key], bucket[i]
#     return bucket
#
# def bucket_sort(arr):
#     buckets = [[] for _ in range(len(arr))]
#
#     #Put array elements in different buckets
#     for num in arr:
#         bi = min(len(arr) -1, int(len(arr) * num))
#         buckets[bi].append(num)
#
#     for bucket in buckets:
#         selection_sort(bucket)
#
#     #Finally concatenate all buckets into arr[]
#     index = 0
#     for bucket in buckets:
#         for value in bucket:
#             arr[index] = value
#             index += 1
#
# array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
# bucket_sort(array)
# print(f"\nSorted array is: ".join(map(str, array)))


class BucketSort:
    @staticmethod
    def insertion_sort(bucket):
        for i in range(len(bucket) - 1):
            for j in range(i, 0, -1):
                if bucket[j] < bucket[j-1]:
                    bucket[j], bucket[j-1] = bucket[j-1], bucket[j]
        return bucket

    def bucket_sort(self, array):
        buckets = [[] for _ in range(len(array))]

        for num in array:
            bi = min(len(array) -1, int(len(array) * num))
            buckets[bi].append(num)

        for bucket in buckets:
            self.insertion_sort(bucket)

        #Join in one arr[]
        index = 0
        for bucket in buckets:
            for value in bucket:
                array[index] = value
                index += 1
        return array

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bs = BucketSort()
print(bs.bucket_sort(arr))