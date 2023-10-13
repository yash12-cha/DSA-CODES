def firstMissingPositive(arr):
    n = len(arr) # Get the length of the input array.
    # Iterate through the array to rearrange elements to their correct positions
    for i in range(n):
        correct_index = arr[i] - 1 # Calculate the correct index for the current element.
        while (arr[i] > 0 and arr[i] <= n and arr[i] != arr[correct_index]):
            # While the current element is a positive integer within the valid range
            # and not in its correct position, swap it with the element at the correct index.
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
            correct_index = arr[i] - 1 # Update the correct index.
    # Iterate through the array again to find the first element not in its correct position.
    for i in range(n):
        if (arr[i] != i + 1):
            # If the element at position i is not equal to i + 1, return i + 1 as the missing integer.
            return i + 1
    # If all positive integers from 1 to n are present, return the next positive integer (n + 1).
    return n + 1
# Input array from the user.
arr = list(map(int,input("Input Array: ").split()))
# Call the function to find the smallest missing positive integer.
res = firstMissingPositive(arr)
# Print the result.
print("Smallest missing positive integer: ",res)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
