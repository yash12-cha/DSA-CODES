class Solution:
    def isSubsetSum (self, N, arr, sum1):
        dp = [[0 for i in range(sum1+1)] for i in range(N+1)]
        for i in range(N + 1):
            dp[i][0] = 1
        for i in range(1, sum1 + 1):
            dp[0][i]= 0
        for i in range(1,N+1):
            for j in range(1,sum1+1):
                if arr[i-1] <= j:
                    dp[i][j] = (dp[i-1][j-arr[i-1]] or dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][sum1]
