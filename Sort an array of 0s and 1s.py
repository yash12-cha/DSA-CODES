def segregate0and1(self, arr, n):
    c0 = 0
    c1 = 0
    c2 = 0
    for i in range(n):
        if arr[i] == 0:
            c0 += 1
        if arr[i] == 1:
            c1 += 1
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
