def leaders(A, N):
    res = []
    max_from_right = -float('inf')
    for i in range(N - 1, -1, -1):
        if A[i] >= max_from_right:
            res.append(A[i])
            max_from_right = A[i]
    res.reverse()
    return res
n = int(input("Input number of elements: "))
arr = list(map(int,input("Enter elements: ").split()))
res = leaders(arr,n)
print("Leaders in the array: ",*res)

'''
Input: -
Input number of elements: 6
Enter elements: 16 17 4 3 5 2

Output: -
Leaders in the array:  17 5 2

Time Complexity: O(n)
'''
