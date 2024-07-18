def binary_search(nums, target, start, end):
    """
    Perform binary search to find the target element in the array between start and end indices.
    
    Args:
    - nums (list of int): The array in which to search.
    - target (int): The element to search for.
    - start (int): The starting index for the search.
    - end (int): The ending index for the search.
    
    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    l, r = start, end
    while l <= r:
        mid = (l + r) // 2  # Calculate the middle index
        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] > target:
            r = mid - 1  # Search in the left half
        else:
            l = mid + 1  # Search in the right half
    return -1  # Target not found

def find_min_index(nums):
    """
    Find the index of the minimum element in the rotated sorted array.
    
    Args:
    - nums (list of int): The rotated sorted array.
    
    Returns:
    - int: The index of the minimum element.
    """
    n = len(nums)
    start, end = 0, n - 1
    
    # If the array is not rotated at all, the first element is the minimum
    if nums[start] < nums[end]:
        return 0
    
    while start <= end:
        mid = start + (end - start) // 2  # Calculate the middle index
        next_index = (mid + 1) % n  # Calculate the next index (circular array)
        prev_index = (mid + n - 1) % n  # Calculate the previous index (circular array)
        
        # Check if the mid element is the minimum
        if nums[mid] <= nums[next_index] and nums[mid] <= nums[prev_index]:
            return mid
        
        # If the right half is sorted, the minimum element must be in the left half
        if nums[mid] <= nums[end]:
            end = mid - 1
        
        # If the left half is sorted, the minimum element must be in the right half
        elif nums[start] <= nums[mid]:
            start = mid + 1
    
    return -1  # In case no minimum is found (shouldn't happen with valid input)

def search(nums, target):
    """
    Search for the target element in a rotated sorted array.
    
    Args:
    - nums (list of int): The rotated sorted array.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    n = len(nums)
    min_index = find_min_index(nums)  # Find the index of the minimum element
    
    # Perform binary search in the two subarrays
    a1 = binary_search(nums, target, 0, min_index - 1)
    a2 = binary_search(nums, target, min_index, n - 1)
    
    # Return the index if found in either subarray
    if a1 != -1:
        return a1
    else:
        return a2

# Input array (rotated sorted array) and target element to search for
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter element to be searched: "))

# Find and print the index of the target element
result = search(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found!!!")

'''
Time complexity of Binary Search is O(log n), where n is the number of elements in the array. It divides the array in half at each step.
Space complexity is O(1) as it uses a constant amount of extra space.
'''
