def knapsack(wt,val,C,n):
    # Base Case
    if n == 0 or C == 0:
        return 0
      
    # choice diagram
    if wt[n-1] <= C:
        return max(val[n-1] + knapsack(wt,val,C-wt[n-1],n-1),knapsack(wt,val,C,n-1))
    else:
        return knapsack(wt,val,C,n-1)
n = int(input())
C = int(input())
val = list(map(int,input().split()))
wt = list(map(int,input().split()))
ans = knapsack(wt,val,C,n)
print(ans)

'''
Input:-
4
40
10 20 30 40
30 10 40 20

Output:-
60

Time Complexity of the above approach is O(2^n).
'''
