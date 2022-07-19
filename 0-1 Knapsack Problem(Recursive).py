def knapsack(wt,val,C,n):
    
    # If number of items is zero or
    # Capacity of knapsack is zero
    if n == 0 or C == 0:
        return 0
    
    # When weight of item is less than or equal to capacity of Knapsack
    if wt[n-1] <= C:
        return max(val[n-1] + knapsack(wt,val,C-wt[n-1],n-1),knapsack(wt,val,C,n-1))
    
    # When weight of item is greater than capacity of Knapsack
    if wt[n-1] > C:
        return knapsack(wt,val,C,n-1)

N = int(input("Enter the number of items: "))
C = int(input("Enter the capacity of knapsack: "))
wt = list(map(int,input("Enter weight of items: ").split()))
val = list(map(int,input("Enter value of items: ").split()))
res = knapsack(wt,val,C,N)
print("Maximum total value in the knapsack: ",res)

'''
Input:-
Enter the number of items: 4
Enter the capacity of knapsack: 40
Enter weight of items: 30 10 40 20
Enter value of items: 10 20 30 40

Output:-
Maximum total value in the knapsack:  60

Time Complexity of the above approach is O(2^n).
'''
