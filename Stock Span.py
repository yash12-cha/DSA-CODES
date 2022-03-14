from collections import deque
def nearestGreatertoLeft(arr, n):
    stack = deque()
    ans = []
    for i in range(0,n,1):
        while (len(stack) != 0 and stack[-1][0] <= arr[i]):
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1][1])
        stack.append([arr[i], i])
    return ans
def stock_span(arr,n):
    result = []
    p = nearestGreatertoLeft(arr,n)
    for i in range(0,n,1):
        result.append(i-p[i])
    return result
n = int(input())
arr = list(map(int,input().split()))
ans = stock_span(arr,n)
print(*ans)

'''
Input:-
7
100 80 60 70 60 75 85

Output:-
1 1 1 2 1 4 6

Time Complexity:O(N), where N is total size of the array

'''
