def nearlySorted(nearly_sorted_array, target):
    left = 0 
    right = len(nearly_sorted_array) - 1  

    while left <= right:
        mid = left + (right - left) // 2  
        if nearly_sorted_array[mid] == target:
            return mid  
        if (mid >=left and nearly_sorted_array[mid-1] == target):
            return mid - 1
        if (mid <=right and nearly_sorted_array[mid+1] == target):
            return mid + 1
        elif target < nearly_sorted_array[mid]:
            right = mid - 2  
        else:
            left = mid + 2 
    
    return -1  

# Input array should be sorted for binary search to work correctly
arr = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter element to be searched: "))

result = nearlySorted(arr, target)
if result != -1:
    print(f"Index of the target element: {result}")
else:
    print("Element not found!!!")
