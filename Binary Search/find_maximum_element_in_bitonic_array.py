def findMaximumBitonicArray(array):
    """
    Finds the index of the maximum element in a bitonic array.
    A bitonic array is first increasing and then decreasing.
    
    :type array: List[int]
    :rtype: int
    """
    n = len(array)  # Length of the array
    left = 0        # Left boundary for binary search
    right = n - 1   # Right boundary for binary search

    # Binary search loop to find the maximum element index
    while left <= right:
        mid = left + (right - left) // 2  # Midpoint calculation to avoid overflow

        # Check if the current element is the maximum
        if mid > 0 and mid < n - 1:
            # If mid is greater than its neighbors, it's the maximum
            if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
                return mid  
            elif array[mid] < array[mid + 1]:
                left = mid + 1  # Maximum must be to the right
            else:
                right = mid - 1  # Maximum must be to the left
        elif mid == 0:
            # Special case: The first element
            if n == 1 or array[0] > array[1]:
                return 0  # Only one element or the first element is the maximum
            else:
                return 1  # The second element is the maximum
        elif mid == n - 1:
            # Special case: The last element
            if array[n - 1] > array[n - 2]:
                return n - 1  # Last element is the maximum
            else:
                return n - 2  # The second last element is the maximum

    return -1  # Return -1 if no maximum found (should not happen in a valid bitonic array)

# Input and result output
arr = list(map(int, input("Enter array elements: ").split()))  # Read input array from the user

result = findMaximumBitonicArray(arr)  # Find the index of the maximum element
if result != -1:
    print(f"Index of the maximum element: {result}")
else:
    print("No Maximum Element found!!!")  # This should not happen in a valid bitonic array
