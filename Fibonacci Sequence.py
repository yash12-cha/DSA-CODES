# Define a function to generate the first 'n' Fibonacci numbers
def fibonacci(n):
    fibonacci_numbers = [0, 1]  # Initialize the list with the first two Fibonacci numbers

    if n <= 0:
        return "Invalid input"  # Handle the case of invalid input

    # Handle the case where n is 1 by returning [0]
    if n == 1:
        return [0]

    for i in range(2, n):
        next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.append(next_number)  # Calculate and append the next Fibonacci number

    return fibonacci_numbers  # Return the list of Fibonacci numbers

# Get the value of n from the user
n = int(input("Enter the value of n: "))
result = fibonacci(n)

if result == "Invalid input":
    print(result)  # Handle and print the "Invalid input" message
else:
    print("The Fibonacci Series is:", *result)  # Print the Fibonacci series

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
