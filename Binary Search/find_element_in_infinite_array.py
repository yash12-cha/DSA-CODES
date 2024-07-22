def binary_search(arr, left, right, target):
    """
    Perform binary search on a sorted array to find the index of the target element.
    
    Args:
    - sorted_array (list of int): The array in which to search.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    while left <= right:
        mid = left + (right - left) // 2  # find the middle element's index to avoid overflow
        if arr[mid] == target:
            return mid  # return the index of the target element
        elif target < arr[mid]:
            right = mid - 1  # discard the right half if mid is greater than target
        else:
            left = mid + 1  # discard the left half if mid is smaller than target
    
    return -1  # target element not found

def find_pos(arr, target):
    """
    Find the position of the target element in an "infinite" sorted array.
    
    Args:
    - arr (list of int): The sorted array in which to search.
    - target (int): The element to search for.
    
    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    low = 0
    high = 1
    
    # Increase the search range exponentially until the target is less than or equal to the element at high
    while target > arr[high]:
        low = high  # Move low to the current high
        high = high * 2  # Double the high index to exponentially expand the search range
    
    # Perform binary search within the defined range
    res = binary_search(arr, low, high, target)
    return res

# Input array should be sorted for binary search to work correctly
arr = list(map(int, input("Enter infinite array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = find_pos(arr, target)
if result != -1:
    print(f"Index of the target element: {result}")
else:
    print("Element not found!!!")

'''
Doubling the high index (high = high * 2) is a strategic choice to efficiently expand the search range while keeping the increase in search space manageable. Here's a more detailed explanation of why doubling is chosen over other multipliers:

1. Smallest Exponential Growth: Doubling (*2) provides the smallest form of exponential growth. This means it increases the search range rapidly but not excessively, ensuring that the search remains efficient and avoids unnecessary large jumps.
2. Balanced Expansion: Doubling strikes a balance between too slow (linear growth like high = high + 1) and too fast (larger multipliers like high = high * 10) range expansion. It ensures that the search space grows quickly enough to cover large ranges but does not overshoot excessively, which would create unnecessarily large search spaces.
3. Optimal Step Size: The step size of doubling is optimal for maintaining efficiency. Larger step sizes (like *3 or *10) would lead to larger and possibly redundant ranges, making the subsequent binary search less efficient. Smaller step sizes (like +1 or *1.5) would result in too many iterations to find the appropriate range, slowing down the process.
'''