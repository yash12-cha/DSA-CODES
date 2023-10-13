def mySqrt(n):
    s = 0
    e = n
    ans = -1  # Initialize the answer to -1 (in case there's no perfect square root)

    while (s <= e):
        mid = (s + e) // 2  # Calculate the midpoint
        if mid * mid == n:  # If the midpoint's square matches the target, return it as the square root
            return mid
        elif mid * mid < n:  # If the square of the midpoint is less than the target, update the answer and move to the right half
            ans = mid
            s = mid + 1
        else:  # If the square of the midpoint is greater than the target, move to the left half
            e = mid - 1

    return ans  # Return the integer part of the square root


def morePrecision(n, precision, temp_res):
    factor = 0.1  # Initialize the factor for the first decimal place
    ans = temp_res

    for i in range(precision):
        while (ans * ans) <= n:  # Repeatedly increase ans by factor until it exceeds n
            ans += factor
        # loop terminates when ans * ans > n
        ans = ans - factor  # Backtrack by subtracting the factor
        factor = factor / 10  # Reduce the factor for the next decimal place

    return round(ans, precision)  # Round the result to the specified precision


n = int(input("Input Number: "))  # Get the input number
temp_res = mySqrt(n)  # Calculate the integer square root
precision = int(input("Input digit up to precision you want: "))  # Get the precision value
res = morePrecision(n, precision, temp_res)  # Calculate the more precise square root
print("Square root of the given number with precision factor: ",res)  # Print the result

'''
Time Complexity : The time required to compute the integral part is O(log(number)) and constant i.e, = precision for computing the fractional part. 
Therefore, overall time complexity is O(log(number) + precision) which is approximately equal to O(log(number)).

Space Complexity: O(1) since it is using constant space for variables.
'''
