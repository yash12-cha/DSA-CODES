def findMinDiff(self, A, n, m):
    A.sort()
    ans = float('inf')
    for i in range(0, n - m + 1):
        mi = A[i]
        ma = A[i + m - 1]
        if ans > ma - mi:
            ans = ma - mi
    return ans
