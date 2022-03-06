# recursive code changes to iterative code
# base case changes to initialisation
def knapsack(wt,val,C,n):
    # defining the matrix and initialising as 0
    dp = [[0 for x in range(C + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, C + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
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
