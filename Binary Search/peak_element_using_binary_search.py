def findPeakElement(array):
    """
    Finds a peak element in the array. A peak element is defined as an element that is greater
    than its neighbors. If the array contains multiple peaks, the function returns the index of any one of them.

    :type array: List[int]
    :rtype: int
    """
    n = len(array)  # Length of the array
    left = 0        # Left boundary for binary search
    right = n - 1   # Right boundary for binary search

    # Binary search loop to find the peak element
    while left <= right:
        mid = left + (right - left) // 2  # Midpoint calculation to avoid overflow

        # Check if the current element is a peak
        if mid > 0 and mid < n - 1:
            if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
                return mid  # Found a peak element
            elif array[mid] < array[mid + 1]:
                left = mid + 1  # Move to the right half
            else:
                right = mid - 1  # Move to the left half
        elif mid == 0:
            # Special case: The first element
            if n == 1 or array[0] > array[1]:
                return 0  # Only one element or the first element is greater than the second
            else:
                return 1  # The second element is the peak
        elif mid == n - 1:
            # Special case: The last element
            if array[n - 1] > array[n - 2]:
                return n - 1  # Last element is the peak
            else:
                return n - 2  # The second last element is the peak

    return -1  # No peak element found (the problem guarantees at least one peak, so this is a safety net)

# Input and result output
arr = list(map(int, input("Enter array elements: ").split()))  # Read input array from the user

result = findPeakElement(arr)  # Find the index of the peak element
if result != -1:
    print(f"Index of the peak element: {result}")
else:
    print("No Peak Element found!!!")  # Shouldn't happen due to problem constraints
