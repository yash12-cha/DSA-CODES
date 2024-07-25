def reverse_binary_search(reverse_sorted_array, target, left, right):
    """
    Performs binary search on a reverse-sorted array to find the target element.

    :param reverse_sorted_array: List[int] - The array sorted in descending order
    :param target: int - The element to search for
    :param left: int - The starting index of the search
    :param right: int - The ending index of the search
    :return: int - The index of the target element if found, otherwise -1
    """
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the mid-point to avoid overflow
        if reverse_sorted_array[mid] == target:
            return mid  # Target found at mid
        elif target < reverse_sorted_array[mid]:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Target not found

def binary_search(nums, target, left, right):
    """
    Performs binary search on a sorted array to find the target element.

    :param nums: List[int] - The array sorted in ascending order
    :param target: int - The element to search for
    :param left: int - The starting index of the search
    :param right: int - The ending index of the search
    :return: int - The index of the target element if found, otherwise -1
    """
    while left <= right:
        mid = (left + right) // 2  # Calculate the mid-point
        if nums[mid] == target:
            return mid  # Target found at mid
        elif nums[mid] > target:
            right = mid - 1  # Search in the left half
        else:
            left = mid + 1  # Search in the right half
    return -1  # Target not found

def find_peak_index(array):
    """
    Finds the index of the peak element in a bitonic array.
    A bitonic array is first increasing and then decreasing.

    :param array: List[int] - The bitonic array
    :return: int - The index of the peak element
    """
    n = len(array)  
    left = 0       
    right = n - 1   
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the mid-point

        # Check if mid is the peak element
        if mid > 0 and mid < n - 1:
            if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
                return mid  # Peak element found
            elif array[mid] < array[mid + 1]:
                left = mid + 1  # Move to the right half
            else:
                right = mid - 1  # Move to the left half
        elif mid == 0:
            # Special case: The first element
            if n == 1 or array[0] > array[1]:
                return 0  # Only one element or the first element is the peak
            else:
                return 1  # The second element is the peak
        elif mid == n - 1:
            # Special case: The last element
            if array[n - 1] > array[n - 2]:
                return n - 1  # Last element is the peak
            else:
                return n - 2  # The second last element is the peak
    return -1  # No peak found (should not happen in a valid bitonic array)

def searchInBitonicArray(nums, target):
    """
    Searches for a target element in a bitonic array.

    :param nums: List[int] - The bitonic array
    :param target: int - The element to search for
    :return: int - The index of the target element if found, otherwise -1
    """
    n = len(nums)
    peak_index = find_peak_index(nums)  # Find the peak element index
    if peak_index == -1:
        return -1  # If no peak, invalid bitonic array

    # Search in the increasing part of the array
    a1 = binary_search(nums, target, 0, peak_index)
    # Search in the decreasing part of the array
    a2 = reverse_binary_search(nums, target, peak_index + 1, n - 1)

    if a1 != -1:
        return a1  # Target found in the increasing part
    else:
        return a2  # Target found in the decreasing part or not found at all

# Input and result output
arr = list(map(int, input("Enter array elements: ").split()))  # Read input array from the user
target = int(input("Enter element to be searched: "))
result = searchInBitonicArray(arr, target)  # Find the index of the target element
if result != -1:
    print(f"Index of the target element: {result}")
else:
    print("Element not found!!!")  # Target element not found in the bitonic array
