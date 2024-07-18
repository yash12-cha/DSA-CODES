def binary_search(sorted_array, target):
    """
    Perform binary search on a sorted array to find the index of the target element.
    
    Args:
    - sorted_array (list of int): The array in which to search.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    left = 0  # index of the leftmost element
    right = len(sorted_array) - 1  # index of the rightmost element

    while left <= right:
        mid = left + (right - left) // 2  # find the middle element's index to avoid overflow
        if sorted_array[mid] == target:
            return mid  # return the index of the target element
        elif target < sorted_array[mid]:
            right = mid - 1  # discard the right half if mid is greater than target
        else:
            left = mid + 1  # discard the left half if mid is smaller than target
    
    return -1  # target element not found

# Input array should be sorted for binary search to work correctly
arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = binary_search(arr, target)
if result != -1:
    print(f"Index of the target element: {result}")
else:
    print("Element not found!!!")
