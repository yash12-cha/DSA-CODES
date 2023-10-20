# Function to merge two sub-arrays
def Merge(Arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    # Create temporary arrays to hold the sub-arrays
    a = [0] * n1
    b = [0] * n2

    z = l
    y = mid + 1

    # Copy data to the temporary arrays a[] and b[]
    for i in range(0, n1):
        a[i] = Arr[z]
        z = z + 1
    for j in range(0, n2):
        b[j] = Arr[y]
        y = y + 1

    i = 0
    j = 0
    k = l

    # Merge the two sub-arrays back into the original array Arr[]
    while i < n1 and j < n2:
        if a[i] < b[j]:
            Arr[k] = a[i]
            k = k + 1
            i = i + 1
        else:
            Arr[k] = b[j]
            k = k + 1
            j = j + 1

    # Copy any remaining elements from the sub-arrays (if any)
    while i < n1:
        Arr[k] = a[i]
        k = k + 1
        i = i + 1
    while j < n2:
        Arr[k] = b[j]
        k = k + 1
        j = j + 1


# Function to perform Merge Sort
def MergeSort(A, l, r):
    if l < r:
        mid = (l + r) // 2

        # Recursively sort the two halves
        MergeSort(A, l, mid)
        MergeSort(A, mid + 1, r)

        # Merge the sorted halves
        Merge(A, l, mid, r)

    return A


# Input array
A = list(map(int, input().split()))

n = len(A)

# Call MergeSort to sort the array
print(*MergeSort(A, 0, n - 1))
