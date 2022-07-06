from collections import deque
def bfsOfGraph(V, adj):
    bfs = [] # List to store result
    visited = [False] * (V+1) # List to keep track of visited nodes
    # Apply BFS for unvisited nodes
    for i in range(1,V+1):
        if visited[i] == False:
            queue = deque() # Initialize a Queue
            # Select vertex i as the root node
            # Add vertex i to queue
            queue.append(i)
            # Mark vertex i as visited
            visited[i] = True
            # If the queue is not empty
            while queue:
                # Remove the first vertex from the queue
                node = queue.popleft()
                bfs.append(node)
                # Insert child nodes of the first vertex into the queue
                for neighbour in adj[node]:
                    if visited[neighbour] == False:
                        visited[neighbour] = True
                        queue.append(neighbour)
    return bfs
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
ans = bfsOfGraph(n,adj)
print("BFS Traversal: ",end=" ")
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
BFS Traversal:  1 2 3 4 5
'''
