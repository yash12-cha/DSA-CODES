def isSubsetSum(n,E,C):
    # defining the matrix and initialising as 0
    dp = [[0 for x in range(C + 1)] for x in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,C+1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, C + 1):
            if E[i-1] <= j:
                dp[i][j] = (dp[i - 1][j - E[i - 1]] or dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][C]
N = int(input("Enter the number of elements: "))
E = list(map(int,input("Enter the elements: ").split()))
S = int(input("Enter Sum: "))
res = isSubsetSum(N,E,S)
if res == 0:
    print("Subset not present.")
else:
    print("Subset present.")

   
'''
Input: -
Enter the number of elements: 6
Enter the elements: 3 34 4 12 5 2
Enter Sum: 9

Output: -
Subset present.

Time Complexity: O(n*C)
'''
