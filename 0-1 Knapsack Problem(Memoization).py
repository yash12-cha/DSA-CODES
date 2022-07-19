def knapsack(wt,val,C,n):
    # defining the matrix and initialising as -1
    # C ---> row
    # n ---> column
    dp = [[-1 for x in range(C + 1)] for x in range(n + 1)]

    # Base Case
    if n == 0 or C == 0:
        return 0

    # checking if -1 is not present then value exists so,return.
    if dp[n][C] != -1:
        return dp[n][C]

    # choice diagram
    if wt[n-1] <= C:
        dp[n][C] = max(val[n-1] + knapsack(wt,val,C-wt[n-1],n-1),knapsack(wt,val,C,n-1))
        return dp[n][C]
    else:
        dp[n][C] = knapsack(wt,val,C,n-1)
        return dp[n][C]
n = int(input())
C = int(input())
val = list(map(int,input().split()))
wt = list(map(int,input().split()))
ans = knapsack(wt,val,C,n)
print(ans)

'''
Input: -
4
40
10 20 30 40
30 10 40 20

Output:-
60

Time Complexity of the above approach is O(n*C).
'''
