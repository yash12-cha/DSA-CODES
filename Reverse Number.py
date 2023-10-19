# Define a function to reverse a number
def reverseNumber(num):
    rev_num = 0
    temp = num  # Initialize a temporary variable to store the number
    while temp > 0:
        remainder = temp % 10
        rev_num = (rev_num * 10) + remainder  # Reverse the number by accumulating the reversed digits
        temp = temp // 10  # Remove the last digit from the temporary variable
    return rev_num

# Get an input number from the user
num = int(input("Input Number: "))

# Call the reverseNumber function to reverse the input number
res = reverseNumber(num)

# Print the reversed number
print("Reversed Number:", res)

'''
Time Complexity: O(log10(n)) - Time complexity for reversing a number, where 'n' is the input number.
Because we are dividing the input number N by 10 in every iteration. So, there is going to be a total of log10(N) iterations.

Space Complexity: O(1) - Constant space used, as the space requirements don't depend on the size of the input number
'''
