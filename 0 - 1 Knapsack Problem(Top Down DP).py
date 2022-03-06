class Solution:
    def knapSack(self,W, wt, val, n):
        dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
        for i in range(1,n + 1):
            for w in range(1,W + 1):
                if wt[i-1] <= w:
                    dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][W]
