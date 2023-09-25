def find3Numbers(A,X):
    n = len(A)
    A.sort()
    for i in range(0, n):
        s = i + 1
        e = n - 1
        while (s < e):
            res = A[i] + A[s] + A[e]
            if res == X:
                return 1
            elif (res > X):
                e = e - 1
            else:
                s = s + 1
    return 0
Arr = list(map(int,input("Input Array: ").split()))
X = int(input("Required Sum: "))
res = find3Numbers(Arr,X)
if res == 1:
    print("Yes triplet is present.")
else:
    print("No triplet is not present.")

'''
Time complexity: O(N^2).
Space Complexity: O(1). 
'''
