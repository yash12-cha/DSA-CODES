def RecursiveBinarySearch(nums, low, high, target):
    # Base Condition
    if low > high:
        return - 1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return RecursiveBinarySearch(nums, low, mid-1,target)
    else:
        return RecursiveBinarySearch(nums, low+1, high,target)

def search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    return RecursiveBinarySearch(nums, low, high, target)

arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = search(arr, target)
if result != -1:
    print(f"Index of the target element: {result}")
else:
    print("Element not found!!!")

# Time Complexity : - O(log2 n)