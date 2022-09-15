def linearsearch(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i
    return -1


N = int(input("Input size of array: "))
arr = list(map(int, input("Input Array: ").split()))
k = int(input("Input element to search: "))
res = linearsearch(arr, N, k)
print("Position at which", k, "is present: ", res)

'''
Input:-
Input size of array: 4
Input Array: 4 2 1 3
Input element to search: 5

Output:-
Position at which 5 is present:  -1

Time Complexity: O(n)
'''
