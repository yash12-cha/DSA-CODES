# Define a function to reverse a string
def reverseString(s):
    # Convert the input string to a list of characters
    s_list = list(s)
    
    # Get the length of the list
    n = len(s_list)
    
    # Initialize two pointers: start and end
    start = 0
    end = n - 1

    # While the start pointer is less than the end pointer
    while start < end:
        # Swap characters at the start and end positions
        s_list[start], s_list[end] = s_list[end], s_list[start]
        # Move the start pointer to the right
        start += 1
        # Move the end pointer to the left
        end -= 1

    # Convert the list of characters back to a string
    reversed_s = "".join(s_list)

    # Return the reversed string
    return reversed_s

# Get an input string from the user
s = input("Input String: ")

# Call the reverseString function to reverse the input string
res = reverseString(s)

# Print the reversed string
print("Reversed String:", res)

'''
Time Complexity: O(n)
Space Complexity: O(n) due to the space used for 's_list'
'''
