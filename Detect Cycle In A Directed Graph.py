from collections import deque
def detectCycleInDirectedGraph(V,adj):
    in_degree = [0 for i in range(V + 1)]
    queue = deque()
    for i in range(V):
        for ne in adj[i]:
            in_degree[ne] += 1

    for i in range(V):
        if in_degree[i] == 0:
            queue.append(i)
    count = 0
    while (queue):
        curr = queue.popleft()
        count += 1
        for ne in adj[curr]:
            in_degree[ne] -= 1
            if in_degree[ne] == 0:
                queue.append(ne)
    if count == V:
        return False
    else:
        return True


# Driver Code
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))
# Adjacency List
adj = [[] for i in range(n+1)]
print("Input Edges: ")
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
ans = detectCycleInDirectedGraph(n,adj)
if ans == True:
    print("Yes there is cycle in the given directed graph.")
else:
    print("No there is no cycle in the given directed graph.")
