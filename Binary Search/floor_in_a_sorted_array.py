def findFloor(sorted_array, target):
    res = -1  # Initialize result to -1, to be used if no floor is found
    left = 0  # Left boundary of the search range
    right = len(sorted_array) - 1  # Right boundary of the search range

    while left <= right:  # Continue searching while the range is valid
        mid = left + (right - left) // 2  # Calculate the mid index to avoid overflow
        if sorted_array[mid] == target:  # If mid element is the target, return its index
            return mid
        if sorted_array[mid] < target:  # If mid element is less than the target
            res = mid  # Update result to the current mid index
            left = mid + 1  # Move the left boundary to the right of mid
        else:  # If mid element is greater than the target
            right = mid - 1  # Move the right boundary to the left of mid
    
    return res  # Return the index of the floor element, or -1 if not found

# Input array should be sorted for binary search to work correctly
arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter element whose floor is to be searched: "))

result = findFloor(arr, target)
if result != -1:
    print(f"Index of floor of the element: {result}")
else:
    print("Floor of element not found!!!")
