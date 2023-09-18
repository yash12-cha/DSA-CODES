def partition(A,s,e):
    pivot = A[s]
    cnt = 0
    for i in range(s+1,e+1):
        if A[i] <= pivot:
            cnt = cnt + 1

    pivotIndex = s + cnt
    A[pivotIndex],A[s] = A[s],A[pivotIndex]
    i = s
    j = e
    while(i < pivotIndex and j > pivotIndex):
        while(A[i] <= pivot):
            i = i + 1
        while(A[j] > pivot):
            j = j - 1
        if(i < pivotIndex and j > pivotIndex):
            A[i],A[j] = A[j],A[i]
            i = i + 1
            j = j - 1
    return pivotIndex



def QuickSort(A, left, right):
    if left < right:
        pi = partition(A, left, right)
        QuickSort(A, left, pi - 1)
        QuickSort(A, pi + 1, right)
    return A
A = list(map(int,input().split()))
n = len(A)
print(*QuickSort(A,0,n-1))
