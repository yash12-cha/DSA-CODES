# Define a function to reverse an array in place
def reverseArray(arr):
    # Get the length of the array
    n = len(arr)

    # Initialize two pointers: start at the beginning and end at the end
    start = 0
    end = n - 1

    # Use a while loop to reverse the array elements
    while start < end:
        # Swap elements at the 'start' and 'end' positions
        arr[start], arr[end] = arr[end], arr[start]
        # Move the 'start' pointer to the right and the 'end' pointer to the left
        start += 1
        end -= 1

    # Return the reversed array
    return arr


# Get input as space-separated integers and convert it into a list
arr = list(map(int, input("Input Array: ").split()))

# Call the reverseArray function to reverse the array
rev = reverseArray(arr)

# Print the reversed array
print("Reversed Array:", *rev)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
