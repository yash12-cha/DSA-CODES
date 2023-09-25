def twoSum(A,X):
    n = len(A)
    A.sort()
    for i in range(0, n):
        s = i
        e = n - 1
        while (s < e):
            res =  A[s] + A[e]
            if res == X:
                return 1
            elif (res > X):
                e = e - 1
            else:
                s = s + 1
    return 0
Arr = list(map(int,input("Input Array: ").split()))
X = int(input("Required Sum: "))
res = twoSum(Arr,X)
if res == 1:
    print("Yes.")
else:
    print("No.")

'''
Time Complexity: O(NlogN), Time complexity for sorting the array
Auxiliary Space: O(1)
'''
