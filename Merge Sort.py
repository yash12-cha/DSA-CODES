def Merge(Arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid
    a = [0] * n1
    b = [0] * n2
    z = l
    y = mid + 1
    for i in range(0, n1):
        a[i] = Arr[z]
        z = z + 1
    for j in range(0, n2):
        b[j] = Arr[y]
        y = y + 1
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if a[i] < b[j]:
            Arr[k] = a[i]
            k = k + 1
            i = i + 1
        else:
            Arr[k] = b[j]
            k = k + 1
            j = j + 1
    while i < n1:
        Arr[k] = a[i]
        k = k + 1
        i = i + 1
    while j < n2:
        Arr[k] = b[j]
        k = k + 1
        j = j + 1

def MergeSort(A, l, r):
    if l < r:
        mid = (l + r) // 2
        MergeSort(A, l, mid)
        MergeSort(A, mid + 1, r)
        Merge(A, l, mid, r)
    return A
A = list(map(int,input().split()))
n = len(A)
print(*MergeSort(A,0,n-1))
