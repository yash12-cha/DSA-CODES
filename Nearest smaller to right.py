from collections import deque
def nearestSmallerToRight(arr, n):
    stack = deque()
    ans = []
    for i in range(n-1,-1,-1):
        while (len(stack) != 0 and stack[-1] >= arr[i]):
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(len(arr))
        stack.append(arr[i])
    ans.reverse()
    return ans
n = int(input())
arr = list(map(int,input().split()))
ans = nearestSmallerToRight(arr,n)
print(*ans)

'''
Input: -
5
6 4 10 2 5

Output:-
4 2 2 -1 -1

Time Complexity: O(N) 
'''
