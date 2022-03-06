from collections import deque
def nextSmallerElement(arr, n):
    stack = deque()
    ans = []
    for i in range(0,n,1):
        while (len(stack) != 0 and stack[-1] >= arr[i]):
            stack.pop()
        if len(stack) == 0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(arr[i])
    return ans
n = int(input())
arr = list(map(int,input().split()))
ans = nextSmallerElement(arr,n)
print(*ans)


