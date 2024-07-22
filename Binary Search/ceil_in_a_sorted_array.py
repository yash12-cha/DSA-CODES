def findCeil(sorted_array, target):
    res = -1  # Initialize result to -1, to be used if no ceil is found
    left = 0  # Left boundary of the search range
    right = len(sorted_array) - 1  # Right boundary of the search range

    while left <= right:  # Continue searching while the range is valid
        mid = left + (right - left) // 2  # Calculate the mid index to avoid overflow
        if sorted_array[mid] == target:  # If mid element is the target, return its index
            return mid
        if sorted_array[mid] < target:  # If mid element is less than the target
            left = mid + 1  # Move the left boundary to the right of mid
        else:  # If mid element is greater than the target
            res = mid  # Update result to the current mid index
            right = mid - 1  # Move the right boundary to the left of mid
    
    return res  # Return the index of the ceil element, or -1 if not found

# Input array should be sorted for binary search to work correctly
arr = list(map(int, input("Enter sorted array elements: ").split()))  # Take sorted array input from user
target = int(input("Enter element whose ceil is to be searched: "))  # Take target element input from user

result = findCeil(arr, target)  # Call findCeil function to get the ceil index
if result != -1:
    print(f"Index of ceil of the element: {result}")  # Print the index of the ceil element
else:
    print("Ceil of element not found!!!")  # Print message if ceil is not found
