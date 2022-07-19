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
N = int(input("Enter the number of items: "))
C = int(input("Enter the capacity of knapsack: "))
wt = list(map(int,input("Enter weight of items: ").split()))
val = list(map(int,input("Enter value of items: ").split()))
res = knapsack(wt,val,C,N)
print("Maximum total value in the knapsack: ",res)


'''
Input: -
Enter the number of items: 4
Enter the capacity of knapsack: 40
Enter weight of items: 30 10 40 20
Enter value of items: 10 20 30 40

Output:-
Maximum total value in the knapsack:  60

Time Complexity of the above approach is O(n*C).
'''
