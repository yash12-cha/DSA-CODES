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

# Define a function to check if a string is a palindrome
def isPalindrome(s):
    # Reverse the input string
    rev_s = reverseString(s)

    # Compare the reversed string to the original string
    if rev_s == s:
        return True
    else:
        return False

# Get an input string from the user
s = input("Input String: ")

# Call the isPalindrome function to check if it's a palindrome
res = isPalindrome(s)

# Check the result and print accordingly
if res == True:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")

# Time and space complexity comments
'''
Time Complexity: O(n) - Linear time complexity due to string reversal
Space Complexity: O(n) - Space used for the list of characters in 's_list'
'''
