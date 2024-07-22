def nextAlphabeticalElement(sorted_array, target):
    res = "*"  # Initialize result to "*" to indicate no element found
    left = 0  # Left boundary of the search range
    right = len(sorted_array) - 1  # Right boundary of the search range

    while left <= right:  # Continue searching while the range is valid
        mid = left + (right - left) // 2  # Calculate the mid index to avoid overflow
        if sorted_array[mid] <= target:  # If mid element is less than or equal to the target
            left = mid + 1  # Move the left boundary to the right of mid
        else:  # If mid element is greater than the target
            res = sorted_array[mid]  # Update result to the current mid element
            right = mid - 1  # Move the right boundary to the left of mid
    
    return res  # Return the next alphabetical element, or "*" if not found

# Input array should be sorted for binary search to work correctly
arr = input("Enter sorted array elements (characters): ").split()  # Take sorted array input from user
target = input("Enter character whose next alphabetical element is to be searched: ")  # Take target character input from user

result = nextAlphabeticalElement(arr, target)  # Call nextAlphabeticalElement function to get the next alphabetical element
if result != "*":
    print(f"Next Alphabetical Element: {result}")  # Print the next alphabetical element
else:
    print("Element not found!!!")  # Print message if no next alphabetical element is found
