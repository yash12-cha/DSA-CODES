# Function to search for a target element in a rotated sorted array
def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid  # Target found at index mid
        
        # Check if the left part is sorted
        if nums[low] <= nums[mid]:
            if (target >= nums[low]) and (target < nums[mid]):
                high = mid - 1  # Adjust the search range to the left part
            else:
                low = mid + 1  # Adjust the search range to the right part
        
        # Check if the right part is sorted
        else:
            if (target > nums[mid]) and (target <= nums[high]):
                low = mid + 1  # Adjust the search range to the right part
            else:
                high = mid - 1  # Adjust the search range to the left part
    
    return -1  # Target element not found

# Input: Read the rotated sorted array and the target element
nums = list(map(int, input("Input Array: ").split()))
target = int(input("Input target element: "))

# Call the search function and print the result
result = search(nums, target)
print(result)


'''
Time Complexity: O(log N) Binary Search requires log N comparisons to find the element.
Space Complexity: O(1)
'''
