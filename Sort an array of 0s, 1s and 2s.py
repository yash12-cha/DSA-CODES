def sort012(arr, n):
    c0, c1, c2 = 0, 0, 0
    for i in range(n):
        if arr[i] == 0:
            c0 += 1
        elif arr[i] == 1:
            c1 += 1
        else:
            c2 += 1
    k = 0
    for i in range(c0):
        arr[k] = 0
        k += 1
    for i in range(c1):
        arr[k] = 1
        k += 1
    for i in range(c2):
        arr[k] = 2
        k += 1

    return arr
n = int(input("Input number of elements: "))
arr = list(map(int,input("Enter elements: ").split()))
res = sort012(arr,n)
print("Sorted array of 0s, 1s and 2s: ",*res)

'''
Input: -
Input number of elements: 5
Enter elements: 0 2 1 2 0

Output: -
Sorted array of 0s, 1s and 2s:  0 0 1 2 2

Time Complexity: O(n). 
'''
