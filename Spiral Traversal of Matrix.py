def spiralOrder(matrix,n):
    ans = []
    top = 0
    left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1

    direc = 0

    while top <= bottom and left <= right:

        if direc == 0:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

        elif direc == 1:
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

        elif direc == 2:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1

        elif direc == 3:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        direc = (direc + 1) % 4

    return ans


# Matrix Size
n = int(input("Input size of matrix: "))
matrix = []
print("Input Matrix: ")
for i in range(n):
    res = list(map(int,input().split()))
    matrix.append(res)
ans = spiralOrder(matrix,n)
print("Spiral Traversal of Matrix: ")
print(ans)


'''
Input:-

Input size of matrix: 3
Input Matrix: 
1 2 3
4 5 6
7 8 9

Output:-

Spiral Traversal of Matrix:
[1, 2, 3, 6, 9, 8, 7, 4, 5]

Time Complexity: O(n^2)
'''
