from collections import deque
def checkForCycle(u,adj,vis):
    # marking the current vertex as visited.
    vis[u] = True
    # create a queue for doing BFS
    queue = deque()
    # enqueue current vertex and its parent info
    queue.append([u,-1])
    # loop till queue is empty
    while queue:
        # dequeue front node from queue
        (v, parent) = queue.popleft()
        # do for every edge (v, u)
        for u in adj[v]:
            if not vis[u]:
                # mark it as visited
                vis[u] = True
                queue.append((u, v))
            # `u` is discovered, and `u` is not a parent
            elif u != parent:
                # we found a cross-edge, i.e., the cycle is found
                return True
    # no cross-edges were found in the graph
    return False
#Function to detect cycle in an undirected graph.
def isCycle(V, adj):
    # using a boolean list to mark all the vertices as not visited.
    visited = [False] * (V)
    # iterating over all the vertices.
    for i in range(V):
        # if vertex is not visited, we call the function to detect cycle.
        if(visited[i] == False):
            # if cycle is found, we return true.
            if checkForCycle(i,adj,visited):
                return True
    return False

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
ans = isCycle(n,adj)
if ans == True:
    print("Yes there is cycle in the given undirected graph.")
else:
    print("No there is no cycle in the given undirected graph.")

'''
Enter number of nodes: 5
Enter number of edges: 5
Input Edges:  0 1
1 2
1 4
4 3
2 3
Yes there is cycle in the given undirected graph.
'''
