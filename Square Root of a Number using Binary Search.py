def mySqrt(n):
    s = 0
    e = n
    ans = -1
    while (s <= e):
        mid = (s + e) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans
n = int(input("Input Number: "))
res = mySqrt(n)
print("Sqaure root of the given Number: ",res)

'''
Time Complexity:- O(log(number))
Space Complexity:- O(1) 
'''
