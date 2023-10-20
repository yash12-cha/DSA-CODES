# Define a function for Bubble Sort
def bubbleSort(Arr, N):
    # Iterate through the elements of the array
    for i in range(N - 1):
        # Initialize a flag to check if any swaps were made in this pass
        swapped = False
        
        # Iterate through the unsorted part of the array
        for j in range(0, N - i - 1):
            # Compare adjacent elements
            if Arr[j] > Arr[j + 1]:
                # Swap the elements if they are in the wrong order
                temp = Arr[j]
                Arr[j] = Arr[j + 1]
                Arr[j + 1] = temp
                # Set the 'swapped' flag to True to indicate a swap was made
                swapped = True
        
        # If no swaps were made in this pass, the array is already sorted, so break out of the loop
        if swapped == False:
            break
    
    # Return the sorted array
    return Arr

# Take input from the user for the size of the array (N) and the array elements (Arr)
N = int(input("Input size of array: "))
Arr = list(map(int, input("Input Array: ").split()))

# Call the bubbleSort function to sort the array
res = bubbleSort(Arr, N)

# Print the sorted array
print("Sorted Array:", *res)


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
