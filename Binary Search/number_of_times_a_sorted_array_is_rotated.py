def find_min_index(nums):
    """
    Find the index of the minimum element in the rotated sorted array.
    
    Args:
    - nums (list of int): The rotated sorted array.
    
    Returns:
    - int: The index of the minimum element.
    """
    n = len(nums)  # Get the length of the array
    start, end = 0, n - 1  # Initialize pointers for the binary search
    
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

def count_rotations(nums):
    """
    Count the number of times the sorted array has been rotated.
    
    Args:
    - nums (list of int): The rotated sorted array.
    
    Returns:
    - int: The number of rotations.
    """
    n = len(nums)  # Get the length of the array
    min_index = find_min_index(nums)  # Find the index of the minimum element
    return min_index

# Input array (rotated sorted array) for which we want to find the number of rotations
arr = list(map(int, input("Enter array elements: ").split()))

# Find and print the number of rotations
result = count_rotations(arr)
print("Number of times the sorted array is rotated: ", result)

'''
Time complexity of Binary Search is O(log n), where n is the number of elements in the array. It divides the array in half at each step.
Space complexity is O(1) as it uses a constant amount of extra space.
'''
