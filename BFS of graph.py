from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
        visited = [False] * (V + 1)  # List to keep track of visited nodes
        queue = deque() # Initialize a Queue
        # Select vertex 0 as the root node
        # Add vertex 0 to queue
        queue.append(0)
        # Mark vertex 0 as visited
        visited[0] = True
        bfs = []
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
