def find_last_occurrence(arr, target):
    """
    Find the last occurrence of the target element in the array.
    
    Args:
    - arr (list of int): The array in which to search.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the last occurrence of the target element if found, otherwise -1.
    """
    left = 0  # index of the leftmost element
    right = len(arr) - 1  # index of the rightmost element
    result = -1  # default result if target is not found
    
    while left <= right:
        mid = left + (right - left) // 2  # calculate the middle index
        if arr[mid] == target:
            result = mid  # update result to the current index
            left = mid + 1  # move right to find the last occurrence
        elif arr[mid] < target:
            left = mid + 1  # discard the left half if mid is smaller than target
        else:
            right = mid - 1  # discard the right half if mid is greater than target
    
    return result

def find_first_occurrence(arr, target):
    """
    Find the first occurrence of the target element in the array.
    
    Args:
    - arr (list of int): The array in which to search.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the first occurrence of the target element if found, otherwise -1.
    """
    left = 0  # index of the leftmost element
    right = len(arr) - 1  # index of the rightmost element
    result = -1  # default result if target is not found
    
    while left <= right:
        mid = left + (right - left) // 2  # calculate the middle index
        if arr[mid] == target:
            result = mid  # update result to the current index
            right = mid - 1  # move left to find the first occurrence
        elif arr[mid] < target:
            left = mid + 1  # discard the left half if mid is smaller than target
        else:
            right = mid - 1  # discard the right half if mid is greater than target
    
    return result

def search_range(nums, target):
    """
    Find the first and last positions of the target element in the array.
    
    Args:
    - nums (list of int): The array in which to search.
    - target (int): The element to search for.
    
    Returns:
    - list of int: A list containing the first and last positions of the target element.
                   If the target is not found, both positions will be -1.
    """
    first_pos = find_first_occurrence(nums, target)  # find the first occurrence
    last_pos = find_last_occurrence(nums, target)  # find the last occurrence
    return [first_pos, last_pos]

# Input array should be sorted for binary search to work correctly
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = search_range(arr, target)
if result[0] != -1:
    print(f"First and last positions of the target element: {result}")
else:
    print("Element not found!!!")

'''
Time complexity of Binary Search is O(log n), where n is the number of elements in the array. It divides the array in half at each step.
Space complexity is O(1) as it uses a constant amount of extra space.
'''
