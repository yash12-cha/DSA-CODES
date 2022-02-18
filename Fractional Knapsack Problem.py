def fractionalKnapsack(w, v, W):
        n = len(w)
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
      
'''
Time Complexity: O(N *log N) where N is the size of the array.
'''
