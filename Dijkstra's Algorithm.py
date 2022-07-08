import heapq
def dijkstra(V, adj, S):
    # Declare empty list.
    minHeap = []
    # using heapify to convert list into min heap.
    heapq.heapify(minHeap)
    # Initialize 'distTo' list with all values as infinite.
    distTo = [ float('inf') for i in range(V+1)]
    # Since the distance of the source node to itself will be 0, update ‘distTo[S]’ to 0.
    distTo[S] = 0
    # Push the source vertex in the Min Heap.
    heapq.heappush(minHeap,[0,S])
    # Loop till all vertices are visited.
    while minHeap:
        # Pop element from the priority queue.
        pair = heapq.heappop(minHeap)

        dist = pair[0]
        prev = pair[1]
        # Iterate through the adjacency list to find all the adjacent vertices to the vertex ‘prev’.
        for it in adj[prev]:
            next = it[0]
            nextDist = it[1]
            if( dist + nextDist < distTo[next] ):
                distTo[next] = dist + nextDist
                heapq.heappush(minHeap,[distTo[next],next])
    return distTo

# Driver Code
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))
# Adjacency List
adjlist = [[] for i in range(n+1)]
print("Input Edges: ",end= " ")
for i in range(0, m):
    # u, v are edges
    # w is weight
    u,v,w = map(int, input().strip().split())
    adjlist[u].append([v,w])
    adjlist[v].append([u,w])
S = int(input("Enter source node: "))
ans = dijkstra(n,adjlist,S)
print("Shortest path from",S,"are: ",end = " ")
for i in range(1,len(ans)):
    print(ans[i],end = " ")

'''
Enter number of nodes: 6
Enter number of edges: 9
Input Edges:  6 1 14
1 2 7
1 3 9
3 2 10
2 4 15
4 5 6
5 6 9
6 3 2
3 4 11
Enter source node: 1
Shortest path from 1 are:  0 7 9 20 20 11 
'''
