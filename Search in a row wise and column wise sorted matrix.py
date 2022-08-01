def searchMatrix(matrix, key):
    n = len(matrix)
    m = len(matrix[0])
    i = 0
    j = m - 1
    while (i >= 0 and i < n and j >= 0 and j < m):
        if matrix[i][j] == key:
            return True
        elif matrix[i][j] > key:
            j -= 1
        elif matrix[i][j] < key:
            i += 1
    return False


# Matrix Size
r = int(input("Input number of rows: "))
c = int(input("Input number of columns: "))
matrix = []
print("Input Matrix: ")
for i in range(r):
    res = list(map(int,input().split()))
    matrix.append(res)
key = int(input("Enter key to search: "))
ans = searchMatrix(matrix,key)
if ans == True:
    print("Element found.")
else:
    print("Element not found.")

'''
Input:-

Input number of rows: 3
Input number of columns: 4
Input Matrix: 
1 3 5 7
10 11 16 20
23 30 34 60
Enter key to search: 13

Output:
Element not found.

Time Complexity: O(row+column)
'''
