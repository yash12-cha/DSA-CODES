def transpose(matrix,n):
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def reverse(matrix):
    for row in matrix:
        row.reverse()
    return matrix

def rotateMatrix(matrix):
    reverse(matrix)
    transpose(matrix,n)
    return matrix
# Matrix Size
n = int(input("Input size of matrix: "))
matrix = []
print("Input Matrix: ")
for i in range(n):
    res = list(map(int,input().split()))
    matrix.append(res)
ans = rotateMatrix(matrix)
print("Matrix rotated by 90 degrees (anti-clockwise): ")
for i in range(len(ans)):
    for j in range(len(ans)):
        print(ans[i][j],end= " ")
    print()

'''
Input:-

Input size of matrix: 3
Input Matrix: 
1 2 3
4 5 6
7 8 9

Output:- 

Matrix rotated by 90 degrees (anti-clockwise): 
3 6 9 
2 5 8 
1 4 7 

Time Complexity: O(n^2)
'''
