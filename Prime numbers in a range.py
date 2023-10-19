from math import sqrt

# Define a function to find prime numbers within a range
def primeRange(start, end):
    primes = []  # Initialize a list to store prime numbers

    for num in range(start, end + 1):
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True  # Assume the number is prime initially
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False  # If a divisor is found, the number is not prime
                    break
            if is_prime:
                primes.append(num)  # If the number is prime, add it to the list

    return primes

# Get the start and end of the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = primeRange(start, end)  # Call the function to find prime numbers
print("Prime numbers between the given range are:", *result)  # Print the prime numbers

'''
Time Complexity: O((end - start + 1) * sqrt(n)), where 'n' is the maximum number in the range.
Space Complexity: O(k), where 'k' is the number of prime numbers in the given range.
'''
