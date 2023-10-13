def pivotIndex(arr):
    arr_sum = 0
    for i in range(len(arr)):
        arr_sum += arr[i]
    left_sum = 0
    right_sum = arr_sum
    for i in range(len(arr)):
        right_sum -= arr[i]
        if (left_sum == right_sum):
            return i
        left_sum += arr[i]
    return -1
arr = list(map(int,input("Input Array: ").split()))
res = pivotIndex(arr)
print("Pivot Index: ",res)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
