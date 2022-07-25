def check(arr1, arr2, n,m):
    # If lengths of arrays are not equal
    if (n != m):
        return False

    # Store arr1 elements and their counts in hash map
    HashMap = {}
    for i in arr1:
        if i in HashMap:
            HashMap[i] += 1
        else:
            HashMap[i] = 1
    #if all elements of arr2[] are present same number
    # of times or not.
    for i in arr2:
        if i not in HashMap:
            return False
        # If an element of arr2 appears more
        # times than it appears in arr1
        if HashMap[i] == 0:
            return False
        HashMap[i] = HashMap[i] - 1
    return True
n = int(input("Input number of elements of first array: "))
arr1 = list(map(int,input("Enter elements: ").split()))
m = int(input("Input number of elements of second array: "))
arr2 = list(map(int,input("Enter elements: ").split()))
res = check(arr1,arr2,n,m)
if res == True:
    print("Two arrays are equal.")
else:
    print("Two arrays are not equal.")
    
'''
Input:
Input number of elements of first array: 3
Enter elements: 1 2 5
Input number of elements of second array: 4
Enter elements: 2 4 1 5

Output:
Two arrays are not equal.

Time Complexity: O(n).
 '''
