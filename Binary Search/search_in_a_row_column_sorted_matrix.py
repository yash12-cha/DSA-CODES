def searchMatrix(matrix, key):
    """
    Searches for a key in a row-wise and column-wise sorted matrix and returns its position.

    :param matrix: List[List[int]] - The matrix to search in, where each row and column is sorted.
    :param key: int - The element to search for.
    :return: tuple - A tuple (i, j) of indices if the element is found, otherwise -1.
    """
    n = len(matrix)    # Number of rows
    m = len(matrix[0]) # Number of columns
    i = 0              # Start at the top-right corner
    j = m - 1

    while i >= 0 and i < n and j >= 0 and j < m:
        if matrix[i][j] == key:
            return (i, j)  # Return the indices (i, j) of the found element
        elif matrix[i][j] > key:
            j -= 1         # Move left
        else:
            i += 1         # Move down

    return -1  # Return -1 if the element is not found

# Input Matrix Size
r = int(input("Input number of rows: "))
c = int(input("Input number of columns: "))
matrix = []
print("Input Matrix: ")
for i in range(r):
    res = list(map(int, input().split()))
    matrix.append(res)

key = int(input("Enter key to search: "))
result = searchMatrix(matrix, key)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")