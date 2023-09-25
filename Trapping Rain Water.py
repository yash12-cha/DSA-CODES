def trappingWater( a, n):
    left = [0] * n
    right = [0] * n
    left[0] = a[0]
    for i in range(1, n):
        left[i] = max(a[i], left[i - 1])

    right[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(a[i], right[i + 1])
    water = [0] * n
    for i in range(n):
        water[i] = min(left[i], right[i]) - a[i]
    ans = sum(water)
    return ans
n = int(input())
arr = list(map(int,input().split()))
ans = trappingWater(arr,n)
print(ans)

'''
Time Complexity: O(N). Only one traversal of the array is needed, So time Complexity is O(N).
Space Complexity: O(N). Extra arrays are needed, each of size N.
'''
