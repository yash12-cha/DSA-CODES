def countDigits(num):
    count_digit = 0
    while num > 0:
        count_digit += 1
        num = num // 10  
    return count_digit
num = int(input("Input Number: "))
res = countDigits(num)
print("Total digits in the given number: ",res)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
