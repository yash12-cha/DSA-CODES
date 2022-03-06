from collections import deque
def nextLargerElement(arr, n):
    stack = deque()
    ans = []
    for i in range(0,n,1):
        while (len(stack) != 0 and stack[-1] <= arr[i]):
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    return ans
n = int(input())
arr = list(map(int,input().split()))
ans = nextLargerElement(arr,n)
print(*ans)


'''
Input: -
5
24 11 13 21 3

Output:-
-1 13 21 -1 -1

Time Complexity: O(N) 
'''
