def minCoins(am,deno):
    M = len(deno)
    ans = []
    deno.sort()
    for i in range(M - 1, -1, -1):
        while (am >= deno[i]):
            am -= deno[i]
            ans.append(deno[i])
    return len(ans)


am = int(input("Input amount: "))
deno = list(map(int,input("Input denominations: ").split()))
res = minCoins(am,deno)
print("Minimum number of coins that add up to the given amount: ",res)

'''
Input:-
Input amount: 49
Input denominations: 2 5 1 50 100 10 20 500 1000

Output:-
Minimum number of coins that add up to the given amount:  5
'''

'''
Time complexity of the Greedy algorithm to find minimum number of coins will be:
1. For sorting denominations O(nlogn).
2. While loop, the worst case is O(amount). If all we have is the coin with 1-denomination.
3. Complexity for Greedy algorithm to find minimum number of coins becomes O(n log n) + O(amount).
'''
