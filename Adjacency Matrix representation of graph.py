# n ----> number of nodes
# m ----> number of edges
n, m = tuple(map(int, input().split()))

# using list comprehension
# to initialize matrix with 0
adjm = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(0, m):
    # Take input of all the edges
    x, y = tuple(map(int, input().split()))
    adjm[x][y] = 1
    adjm[y][x] = 1
print("Adjacency matrix of above graph is given by: ")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(adjm[i][j], end=" ")
    print()
    
'''
Input: -
7 7
1 2
1 3
2 4
2 5
2 6
2 7
7 3
Output: -
Adjacency matrix of above graph is given by: 
0 1 1 0 0 0 0 
1 0 0 1 1 1 1 
1 0 0 0 0 0 1 
0 1 0 0 0 0 0 
0 1 0 0 0 0 0 
0 1 0 0 0 0 0 
0 1 1 0 0 0 0
'''

