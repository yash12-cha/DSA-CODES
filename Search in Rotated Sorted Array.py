def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # Left Part is sorted
        if nums[low] <= nums[mid]:
            if (target >= nums[low]) and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right Part is sorted
        else:
            if (target > nums[mid]) and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
nums = list(map(int,input("Input Array: ").split()))
target = int(input("Input target element: "))
print(search(nums,target))

'''
Time Complexity: O(log N) Binary Search requires log N comparisons to find the element.
Space Complexity: O(1)
'''
