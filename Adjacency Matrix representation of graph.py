# n ----> number of nodes
# m ----> number of edges
n,m = tuple(map(int,input().split()))

# using list comprehension
# to initialize Adjacency Matrix with 0
adj = [[0 for i in range(n+1)]for j in range(n+1)]

for i in range(0,m):
    x, y = tuple(map(int, input().split()))
    adj[u][v] =1
    adj[v][u] = 1

    
 '''
 Space Complexity: O(n^2), where n is number of nodes
 '''
