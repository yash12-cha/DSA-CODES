def bubbleSort(Arr, N):
    for i in range(N - 1):
        swapped = False
        # (N - i - 1) is for ignoring comparisons of elements which have already been compared in earlier iterations
        for j in range(0, N - i - 1):
            if Arr[j] > Arr[j + 1]:
                temp = Arr[j]
                Arr[j] = Arr[j + 1]
                Arr[j + 1] = temp
                swapped = True
        # If no number was swapped that means array is sorted now, break the loop.
        if swapped == False:
            break
    return Arr
N = int(input("Input size of array: "))
Arr = list(map(int,input("Input Array: ").split()))
res = bubbleSort(Arr, N)
print("Sorted Array:",*res)

'''
Input:-
Input size of array: 5
Input Array: 4 1 3 9 7

Output:-
Sorted Array: 1 3 4 7 9

Time Complexities:-
1. Worst Case Complexity: O(n2) If we want to sort in ascending order and the array is in descending order then the worst case occurs.
2. Best Case Complexity: O(n) If the array is already sorted, then there is no need for sorting.
3. Average Case Complexity: O(n2) It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

'''
