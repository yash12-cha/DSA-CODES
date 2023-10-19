# Define a function to check if a number is an Armstrong number
def is_armstrong_number(num):
    # Calculate the order (number of digits) in the given number
    order = len(str(num))
    # Initialize the sum to 0
    sum = 0
    # Create a temporary variable to iterate through the digits
    temp = num
    # Iterate through the digits of the number
    while temp > 0:
        # Get the last digit of the number
        digit = temp % 10
        # Add the digit raised to the power of the order to the sum
        sum += digit ** order
        # Remove the last digit by integer division
        temp //= 10
    # Check if the original number is equal to the calculated sum
    if num == sum:
        return True  # It's an Armstrong number
    else:
        return False  # It's not an Armstrong number

# Define a function to find Armstrong numbers within a given range
def find_armstrong_numbers_in_range(start, end):
    # Initialize an empty list to store Armstrong numbers
    armstrong_numbers = []
    # Iterate through numbers in the specified range
    for num in range(start, end + 1):
        # Check if the current number is an Armstrong number
        if is_armstrong_number(num):
            # If it is, add it to the list of Armstrong numbers
            armstrong_numbers.append(num)
    # Return the list of Armstrong numbers found in the range
    return armstrong_numbers

# Get the start and end of the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Call the function to find Armstrong numbers in the specified range
armstrong_numbers = find_armstrong_numbers_in_range(start, end)

# Display the Armstrong numbers found in the range
print("Armstrong numbers between the given range are: ",*armstrong_numbers)

'''
Time Complexity: O((end - start) * log10(N)).
Because we are dividing the input number N by 10 in every iteration. So, there is going to be a total of log10(N) iterations.

Space Complexity: O(N) where "N" is the number of Armstrong numbers found in the given range.
'''
