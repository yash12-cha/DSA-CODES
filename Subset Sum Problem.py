def isSubsetSum(N, arr, S):
    # Create a 2D list to store the DP table
    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
    
    # If sum is 0, then answer is true (empty subset)
    for i in range(N+1):
        dp[i][0] = 1
    
    # If there are no elements and sum is not 0, then answer is false
    for i in range(1, S+1):
        dp[0][i] = 0
    
    # Fill the rest of the DP table
    for i in range(1, N+1):
        for j in range(1, S+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[N][S]
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

Time Complexity: O(N*S)
'''
