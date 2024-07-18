def find_min(nums):
    n = len(nums)
    start, end = 0, n - 1
    if nums[start] < nums[end]:
        return 0
    while start <= end:
        mid = start + (end - start) // 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n
        if nums[mid] <= nums[next] and nums[mid] <= nums[prev]:
            return mid
        if nums[mid] <= nums[end]:
            end = mid - 1
        elif nums[start] <= nums[mid]:
            start = mid + 1
    return -1

def countRotations(nums):
    n = len(nums)
    min_index = find_min(nums)
    return min_index

# Input array should be sorted for binary search to work correctly
arr = list(map(int, input("Enter array elements: ").split()))

result = countRotations(arr)

print("Number of times the sorted array is rotated: ", result)

'''
Time complexity of Binary Search is O(log n), where n is the number of elements in the array. It divides the array in half at each step.
Space complexity is O(1) as it uses a constant amount of extra space.
'''
