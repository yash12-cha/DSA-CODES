def insertionSort(Arr, N):
    for i in range(1, N):
        current = Arr[i]
        j = i - 1
        while (j >= 0 and Arr[j] > current):
            Arr[j + 1] = Arr[j]
            j = j - 1
        Arr[j + 1] = current
    return Arr

N = int(input("Input size of array: "))
Arr = list(map(int,input("Input Array: ").split()))
res = insertionSort(Arr, N)
print("Sorted Array:",*res)

'''
Input:-
Input size of array: 5
Input Array: 4 1 3 9 7

Output:-
Sorted Array: 1 3 4 7 9

Time Complexities:-

1. Worst Case Complexity: O(n^2) Suppose, an array is in ascending order, and you want to sort it in descending order. In this case, worst case complexity occurs.
2. Best Case Complexity: O(n) When the array is already sorted, the outer loop runs for n number of times whereas the inner loop does not run at all. So, there are only n number of comparisons. Thus, complexity is linear.
3. Average Case Complexity: O(n^2) It occurs when the elements of an array are in jumbled order (neither ascending nor descending).

'''
