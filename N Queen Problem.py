# Python program to solve n-queens problem

# Function to check if placing queen to board[row][col] is safe.
def isSafe(board, row, col, n):
    i = row - 1
    # Check this coloumn.
    while i >= 0:
        if board[i][col] == 'Q':
            return False
        i = i - 1
    i = row - 1
    j = col - 1
    # Check upper - left diagonal.
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    i = row - 1
    j = col + 1
    # Check upper - right diagonal.
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True


def solve(row, n, board):
    # if `n` queens are placed successfully, print the solution
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
        print()

    # Consider current column and try placing
    # queen in all rows one by one
    for col in range(n):
        # Check if placing queen to board[row][col] is safe.
        if isSafe(board, row, col, n, ):
            # Place this queen in board[row][col]
            board[row][col] = 'Q'
            # move ahead for next row
            solve(row + 1, n, board)
            # If placing queen in board[row][col]
            # doesn't lead to a solution, then
            # remove queen from board[row][col]
            board[row][col] = '.' # Backtracking Step

# It mainly uses solve() to solve the problem.
def solveNQueens(n):
    # Creating n x n chessboard and initialising it with '.'
    board = [['.' for i in range(n)] for j in range(n)]
    # call solve() initially for 0th row
    solve(0, n, board)

# Input number of Queens
n = int(input("Input value of n: "))
print()
print("All distinct ways of placing n queens on an n x n chessboard: ")
# This function solves the N Queen problem using Backtracking.
solveNQueens(n)

'''
Input:-
Input value of n: 4

Output:-
All distinct ways of placing n queens on an n x n chessboard: 
. Q . . 
. . . Q 
Q . . . 
. . Q . 

. . Q . 
Q . . . 
. . . Q 
. Q . . 

'''

'''
Time Complexity:-
O(N!), where ‘N’ is the number of queens and ‘!’ represents factorial.
For the first column, we check ‘N’ rows, for the second column we check 'N - 1 row and so on. hence time complexity will be N * (N-1) * (N-2) …. i.e N!
'''
