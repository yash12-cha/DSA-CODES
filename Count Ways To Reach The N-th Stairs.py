def countWays(nStairs):
    mod = 1000000007
    dp = [0] * (nStairs + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, nStairs + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    return dp[nStairs]

N = int(input("Number of stairs: "))
r = countWays(N)
print("Number of ways to reach the nth stair: ",r)

'''
Number of stairs: 4
Number of ways to reach the nth stair:  5
'''

'''
Time Complexity:-

O(N), Where ‘N’ is the number of stairs.

We are traversing in “dp” only once to fill the”dp”. So time complexity will be O(N).
'''
