from collections import deque
def dfsOfGraph(V, adj):
    dfs = [] # List to store result
    visited = [False] * (V+1) # List to keep track of visited nodes
    # Apply DFS for unvisited nodes
    for i in range(1,V+1):
        if visited[i] == False:
            stack = deque() # Initialize a Stack
            # Select vertex i as the root node
            # Add vertex i to stack
            stack.append(i)
            # If the stack is not empty
            while stack:
                # Remove the first vertex from the stack
                node = stack.pop()
                if (not visited[node]):
                    dfs.append(node)
                    visited[node] = True
                for neighbor in adj[node]:
                    if (not visited[neighbor]):
                        stack.append(neighbor)
    return dfs
# Driver Code
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))
# Adjacency List
adj = [[] for i in range(n+1)]
print("Input Edges: ",end= " ")
for i in range(0,m):
    x, y = tuple(map(int, input().split()))
    adj[x].append(y)
    adj[y].append(x)
ans = dfsOfGraph(n,adj)
print("DFS Traversal: ",end=" ")
print(*ans)


'''
Enter number of nodes: 5
Enter number of edges: 6
Input Edges:  1 2
1 3
2 4
2 3
4 5
3 5
DFS Traversal:  1 3 5 4 2
'''
