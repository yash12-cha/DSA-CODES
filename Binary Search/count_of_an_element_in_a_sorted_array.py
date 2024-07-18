def find_last_occurrence(arr, n, target):
    """
    Find the last occurrence of the target element in the array.
    
    Args:
    - arr (list of int): The array in which to search.
    - n (int): The size of the array.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the last occurrence of the target element if found, otherwise -1.
    """
    left = 0  # index of the leftmost element
    right = n - 1  # index of the rightmost element
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

def find_first_occurrence(arr, n, target):
    """
    Find the first occurrence of the target element in the array.
    
    Args:
    - arr (list of int): The array in which to search.
    - n (int): The size of the array.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the first occurrence of the target element if found, otherwise -1.
    """
    left = 0  # index of the leftmost element
    right = n - 1  # index of the rightmost element
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

def count_occurrences(arr, n, target):
    """
    Count the number of occurrences of the target element in the array.
    
    Args:
    - arr (list of int): The array in which to search.
    - n (int): The size of the array.
    - target (int): The element to search for.
    
    Returns:
    - int: The count of occurrences of the target element in the array.
    """
    first_occurrence = find_first_occurrence(arr, n, target)
    last_occurrence = find_last_occurrence(arr, n, target)
    if first_occurrence == -1 or last_occurrence == -1:  # If the element is not found
        return 0
    return last_occurrence - first_occurrence + 1

# Input array should be sorted for binary search to work correctly
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = count_occurrences(arr, len(arr), target)
if result == 0:
    print("Element not present. So count is Zero.")
else:
    print("Count of the element: ", result)

'''
Time complexity of Binary Search is O(log n), where n is the number of elements in the array. It divides the array in half at each step.
Space complexity is O(1) as it uses a constant amount of extra space.
'''

