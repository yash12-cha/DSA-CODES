def fractionalKnapsack(n,w, v, W):
    # Combine value and weight of items in single list
    a = []
    for i in range(n):
        l = []
        l.append(v[i])
        l.append(w[i])
        a.append(l)
    # Sort items in decreasing order of value / weight ratio
    a.sort(key=lambda x: x[0] / x[1], reverse=True)
    totalValue = 0

    for i in range(n):
        curr_wei = a[i][1]
        curr_val = a[i][0]
        # Add the whole item if the current weight is less than the capacity of the knapsack
        if W - curr_wei >= 0:
            W -= curr_wei
            totalValue += curr_val
        # Else add a portion of the item to the knapsack
        else:
            totalValue += curr_val * W / curr_wei
            break
    return int(totalValue)
n = int(input("Input number of items: "))
C = int(input("Input capacity of knapsack: "))
w = list(map(int,input("Input weight of items: ").split()))
v = list(map(int,input("Input values of items: ").split()))
res = fractionalKnapsack(n,w,v,C)
print("Maximum total value in the knapsack: ",res)

'''
Input:-
Input number of items: 3
Input capacity of knapsack: 50
Input weight of items: 10 20 30
Input values of items: 60 100 120

Output:-
Maximum total value in the knapsack:  240
'''
      
'''
Time Complexity: O(n log n + n). O(n log n) to sort the items and O(n) to iterate through all the items for calculating the answer.
'''
