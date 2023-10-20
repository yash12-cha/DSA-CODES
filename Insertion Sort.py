# Define a function for Insertion Sort
def insertionSort(Arr, N):
    # Iterate through the elements of the array starting from the second element (index 1)
    for i in range(1, N):
        # Store the current element to be inserted into the sorted portion
        current = Arr[i]
        j = i - 1

        # Move elements of the sorted portion that are greater than 'current' to the right
        while j >= 0 and Arr[j] > current:
            Arr[j + 1] = Arr[j]
            j = j - 1

        # Insert the 'current' element into its correct sorted position
        Arr[j + 1] = current

    # Return the sorted array
    return Arr

# Take input from the user for the size of the array (N) and the array elements (Arr)
N = int(input("Input size of array: "))
Arr = list(map(int, input("Input Array: ").split()))

# Call the insertionSort function to sort the array
res = insertionSort(Arr, N)

# Print the sorted array
print("Sorted Array:", *res)

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
