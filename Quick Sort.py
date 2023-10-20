# Function to partition the array and return the pivot index
def partition(A, s, e):
    pivot = A[s]  # Choose the first element as the pivot
    cnt = 0
    
    # Count the number of elements less than or equal to the pivot
    for i in range(s + 1, e + 1):
        if A[i] <= pivot:
            cnt = cnt + 1
    
    pivotIndex = s + cnt
    
    # Swap the pivot element with the element at the pivotIndex
    A[pivotIndex], A[s] = A[s], A[pivotIndex]
    
    i = s
    j = e
    
    # Perform the partitioning
    while i < pivotIndex and j > pivotIndex:
        while A[i] <= pivot:
            i = i + 1
        while A[j] > pivot:
            j = j - 1
        if i < pivotIndex and j > pivotIndex:
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j = j - 1
    
    return pivotIndex

# Function to perform Quick Sort
def QuickSort(A, left, right):
    if left < right:
        pi = partition(A, left, right)  # Get the pivot index
        
        # Recursively sort the sub-arrays before and after the pivot
        QuickSort(A, left, pi - 1)
        QuickSort(A, pi + 1, right)
    
    return A

# Input array
A = list(map(int, input().split()))

n = len(A)

# Call QuickSort to sort the array
print(*QuickSort(A, 0, n - 1))
