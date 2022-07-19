def knapsack(wt,val,C,n):
    # defining the matrix and initialising as -1
    # C ---> column
    # n ---> row
    dp = [[-1 for x in range(C + 1)] for x in range(n + 1)]

    # Base Case
    # If number of items is zero or
    # Capacity of knapsack is zero
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
