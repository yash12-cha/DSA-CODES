def findNthRootOfM(n, m):
    low = 1
    high = m
    eps = 1e-7
    # Keep searching for the ‘N’th root until the difference between
    # higher bound and lower bound is very less (i.e. in order of 10^-7)
    while ((high - low) > eps):
        mid = (low + high) / 2
        if (mid ** n) < m:
            low = mid
        else:
            high = mid

    return format(low, ".6f")
n = int(input("Input the value of n: "))
m = int(input("Input number: "))
r = findNthRootOfM(n,m)
print(n,"th root of",m,"is: ",r)

'''
Input the value of n: 3
Input number: 27
3 th root of 27 is:  3.000000
'''

'''
Time Complexity:-

O( log(N) * log(M) ), Where ‘N’ and ‘M’ are input integers.

In the above algorithm, the search space is ‘M’, and hence in ‘log(M)’ iterations we will find the ‘N’th root, and in each iteration, 
we find the ‘N’th power of ‘MIDDLE’ using binary exponentiation which takes ‘log( N )’ iterations, thus in total ‘log(N)*log(M)’ iterations. 

Hence the time complexity will be O( log(N) * log(M) )
'''
