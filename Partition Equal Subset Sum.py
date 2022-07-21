def isSubsetSum(E,C):
    n = len(E)
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

def canPartition(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    if sum % 2 != 0:
        return False
    else:
        return isSubsetSum(nums, sum // 2)
N = int(input("Enter the number of elements: "))
E = list(map(int,input("Enter the elements: ").split()))
res = canPartition(E)
if res == True:
    print("Array can be partitioned.")
else:
    print("Array cannot be partitioned.")

'''
Input:-
Enter the number of elements: 4
Enter the elements: 1 2 3 5

Output:-
Array cannot be partitioned.

Time Complexity:- O(sum*n) 
'''
