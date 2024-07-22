# Search in an almost sorted array

'''
An "almost sorted" array refers to an array where each element is either in its correct position or close to its correct position relative to the fully sorted order. 
An element can be at (i)th position or (i+1)th position or (i-1)th position.
'''
def nearlySorted(nearly_sorted_array, target):
    left = 0 
    right = len(nearly_sorted_array) - 1  

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        if nearly_sorted_array[mid] == target:
            return mid  # Return the index if the middle element is the target

        # Check the elements adjacent to the middle (if they exist)
        if mid - 1 >= left and nearly_sorted_array[mid - 1] == target:
            return mid - 1  # Return the index if the element before middle is the target

        if mid + 1 <= right and nearly_sorted_array[mid + 1] == target:
            return mid + 1  # Return the index if the element after middle is the target

        # Adjust the search range based on comparison with the middle element
        elif target < nearly_sorted_array[mid]:
            right = mid - 2  # Update the right boundary if target is less than middle element
        else:
            left = mid + 2  # Update the left boundary if target is greater than middle element
    
    return -1  # Return -1 if target element is not found


arr = list(map(int, input("Enter nearly sorted array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = nearlySorted(arr, target)
if result != -1:
    print(f"Index of the target element: {result}")
else:
    print("Element not found!!!")
