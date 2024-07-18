def reverse_binary_search(reverse_sorted_array, target):
    """
    Perform binary search on a reverse sorted array to find the index of the target element.
    
    Args:
    - reverse_sorted_array (list of int): The array in which to search.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    left = 0  # index of the leftmost element
    right = len(reverse_sorted_array) - 1  # index of the rightmost element

    while left <= right:
        mid = left + (right - left) // 2  # find the middle element's index to avoid overflow
        if reverse_sorted_array[mid] == target:
            return mid  # return the index of the target element
        elif target < reverse_sorted_array[mid]:
            left = mid + 1  # discard the left half if mid is greater than target
        else:
            right = mid - 1  # discard the right half if mid is smaller than target
    
    return -1  # target element not found

# Input array should be reverse sorted for binary search to work correctly
arr = list(map(int, input("Enter reverse sorted array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = reverse_binary_search(arr, target)
if result != -1:
    print(f"Index of the target element: {result}")
else:
    print("Element not found!!!")

'''
Time complexity of Binary Search is O(log n), where n is the number of elements in the array. It divides the array in half at each step. 
Space complexity is O(1) as it uses a constant amount of extra space.
'''