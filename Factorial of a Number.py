def factorial(N):
    fact = 1
    if N < 0:
        return "Does Not Exist!!!"
    elif N == 0:
        return 1
    while (N):
        fact = fact * N
        N = N - 1
    return fact

num = int(input("Input Number: "))
res = factorial(num)
print("Factorial of the given number: ",res)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
