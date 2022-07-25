def getMissingNo(arr, n):
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(arr)
    return total - sum_of_A
n = int(input("Input number of elements: "))
arr = list(map(int,input("Enter elements: ").split()))
res = int(getMissingNo(arr,n))
print("Missing Number: ",res)

'''
Input:-
Input number of elements: 4
Enter elements: 1 2 3 5

Output:-
Missing Number:  4

Time Complexity: O(N)
'''
