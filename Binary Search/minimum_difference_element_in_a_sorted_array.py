def binarySearchMinDifference(sorted_array, target):
    """
    This function finds the element in the sorted array that is closest to the target.
    If the target is found, it returns the target itself. Otherwise, it returns the 
    closest element to the target.

    :param sorted_array: List[int] - A list of sorted integers.
    :param target: int - The target value to find or approximate.
    :return: int - The closest element to the target in the array.
    """
    
    left = 0  
    right = len(sorted_array) - 1  

    # Perform binary search to find the closest or exact match
    while left <= right:
        mid = left + (right - left) // 2  # Find the mid-point
        if sorted_array[mid] == target:
            return sorted_array[mid]  # Target found, return it
        elif target < sorted_array[mid]:
            right = mid - 1  # Target is in the left half
        else:
            left = mid + 1  # Target is in the right half
    
    # Check if left has gone out of bounds
    if left >= len(sorted_array):
        return sorted_array[right]
    # Check if right has gone out of bounds
    elif right < 0:
        return sorted_array[left]
    
    # Determine which of the boundary elements is closer to the target
    if abs(sorted_array[right] - target) < abs(sorted_array[left] - target):
        return sorted_array[right]
    else:
        return sorted_array[left]
    
# Input and output handling
arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = binarySearchMinDifference(arr, target)
print(f"Closest element to the target: {result}")
