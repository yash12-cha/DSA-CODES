def getMissingNo(arr):
    # get the array's length
    n = len(arr)
    # actual size is `n+1` since a number is missing from the list
    m = n + 1
    # get sum of integers between 1 and `n+1` using the formula N * (N+1)/2.
    total = m * (m + 1) // 2
    # the missing number is the difference between the expected sum and
    # the actual sum of integers in the list
    return total - sum(arr)
n = int(input("Input number of elements: "))
arr = list(map(int,input("Enter elements: ").split()))
res = int(getMissingNo(arr))
print("Missing Number: ",res)

'''
Input:-
Input number of elements: 4
Enter elements: 1 2 3 5

Output:-
Missing Number:  4

Time Complexity: O(N)
'''
