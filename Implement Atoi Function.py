def atoi(s):
    n = len(s)
    number = 0
    isNegative = 0
    
    # Check Negative.
    if (s[0] == '-'):
        isNegative = 1
        
    for i in range(n):
        # If the charecter is a digit.
        if (s[i] >= '0' and s[i] <= '9'):
            digit = ord(s[i]) - ord('0')
            number = number * 10 + digit
        else:
            return -1
        
    if (isNegative):
        number *= -1
    return number
s = input("Input String: ")
res = atoi(s)
if res == -1:
    print("No valid conversion takes place.")
else:
    print("Equivalent integer number for the passed string number: ",res)
    
    
'''
Input:-
Input String: 32a

Output:-
No valid conversion takes place.

Time Complexity:-
O(N), where ‘N’ denotes the length of the string.
'''
