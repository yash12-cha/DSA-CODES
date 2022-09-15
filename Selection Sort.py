def selectionSort(Arr, N):
    for i in range(0, N - 1):
        mini = i
        for j in range(i + 1, N):
            if Arr[j] < Arr[mini]:
                mini = j
        temp = Arr[i]
        Arr[i] = Arr[mini]
        Arr[mini] = temp
    return Arr

N = int(input("Input size of array: "))
Arr = list(map(int,input("Input Array: ").split()))
res = selectionSort(Arr, N)
print("Sorted Array:",*res)


'''
Input:-
Input size of array: 5
Input Array: 20 12 10 5 2

Output:-
Sorted Array: 2 5 10 12 20

Time Complexities:-
1. Worst Case Complexity: O(n^2) If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
2. Best Case Complexity: O(n^2) It occurs when the array is already sorted
3. Average Case Complexity: O(n^2) It occurs when the elements of the array are in jumbled order (neither ascending nor descending).
'''
