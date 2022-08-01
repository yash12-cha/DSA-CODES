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
    transpose(matrix, n)
    reverse(matrix)
    return matrix
# Matrix Size
n = int(input("Input size of matrix: "))
matrix = []
print("Input Matrix: ")
for i in range(n):
    res = list(map(int,input().split()))
    matrix.append(res)
ans = rotateMatrix(matrix)
print("Matrix rotated by 90 degrees (clockwise): ")
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
Matrix rotated by 90 degrees (clockwise): 
7 4 1 
8 5 2 
9 6 3 

Time Complexity:- O(n^2)
'''
