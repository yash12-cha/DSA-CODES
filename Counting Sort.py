def countingSort(self,Arr, N):
    maxi = Arr[0]
    for i in range(N):
        if Arr[i] > maxi:
            maxi = Arr[i]
    # Initialize count array
    Count = [0] * (maxi + 1)
    # Store the count of each elements in count array
    for i in range(N):
        Count[Arr[i]] = Count[Arr[i]] + 1
    # Store the cummulative count
    for i in range(1, maxi + 1):
        Count[i] = Count[i] + Count[i - 1]
    # Find the index of each element of the original array in count array
    # place the elements in output array
    output = [0] * (N)
    for i in range(N - 1, -1, -1):
        Count[Arr[i]] -= 1
        output[Count[Arr[i]]] = Arr[i]
    # Copy the sorted elements into original array
    for i in range(N):
        Arr[i] = output[i]
    return Arr
