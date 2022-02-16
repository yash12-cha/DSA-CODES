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

