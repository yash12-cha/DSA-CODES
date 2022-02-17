from collections import deque
class Solution:
     def dfsOfGraph(self, V, adj):
        visited = [False] * (V+1) # List to keep track of visited nodes
        stack = deque() # Initialize a Stack
        # Select vertex 0 as the root node
        # Add vertex 0 to stack
        stack.append(0)
        dfs = []
        # If the queue is not empty
        while stack:
            # Remove the first vertex from the stack
            node = stack.pop()
            if (not visited[node]):
                dfs.append(node)
                visited[node] = True
            for neighbor in reversed(adj[node]):
                if (not visited[neighbor]):
                    stack.append(neighbor)
        return dfs
