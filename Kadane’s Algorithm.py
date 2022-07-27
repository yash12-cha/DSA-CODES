def kadane(arr):
    n = len(arr)
    maxi = -float('inf')
    max_till_here = 0
    for i in range(n):
        max_till_here = max_till_here + arr[i]
        if maxi < max_till_here:
            maxi = max_till_here
        if max_till_here < 0:
            max_till_here = 0
    return maxi

n = int(input("Enter number of elements: "))
arr = list(map(int,input("Enter elements: ").split()))
res = kadane(arr)
print("Maximum Subarray Sum: ",res)


'''
Input:
Enter number of elements: 8
Enter elements: -2 -3 4 -1 -2 1 5 -3

Output:
Maximum Subarray Sum:  7

Time Complexity: O(n)
'''
