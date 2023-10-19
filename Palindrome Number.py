# Define a function to reverse a number
def reverseNumber(num):
    rev_num = 0
    temp = num  # Initialize a temporary variable to store the number
    while temp > 0:
        remainder = temp % 10
        rev_num = (rev_num * 10) + remainder  # Reverse the number by accumulating the reversed digits
        temp = temp // 10  # Remove the last digit from the temporary variable
    return rev_num

# Define a function to check if a number is a palindrome
def isPalindrome(num):
    # Reverse the input number
    rev_num = reverseNumber(num)

    # Compare the reversed number to the original number
    if rev_num == num:
        return True
    else:
        return False

# Get an input number from the user
num = int(input("Input Number: "))

# Call the isPalindrome function to check if it's a palindrome
res = isPalindrome(num)

# Check the result and print accordingly
if res == True:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")


'''
Time Complexity: O(log10(n)) - Time complexity for reversing a number, where 'n' is the input number.
Because we are dividing the input number N by 10 in every iteration. So, there is going to be a total of log10(N) iterations.

Space Complexity: O(1) - Constant space used, as the space requirements don't depend on the size of the input number
'''
