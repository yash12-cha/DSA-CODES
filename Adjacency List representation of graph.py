# n ----> number of nodes
# m ----> number of edges
n, m = tuple(map(int, input().split()))

adjlist = [[] for i in range(n+1)]

for i in range(0, m):
    # Take input of all the edges
    x, y = tuple(map(int, input().split()))
    adjlist[x].append(y)
    adjlist[y].append(x)
print("Adjacency list of above graph is given by: ")
for i in range(1, n + 1):
    print(i,end="->")
    for j in adjlist[i]:
        print(j,end=" ")
    print()

'''
Space Complexity: O(n+2m), where n is number of nodes and m is number of edges.

'''
