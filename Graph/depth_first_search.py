from collections import deque

class DepthFirstSearch:
    def build_graph(self, edges, num_vertices):
        """
        Build an adjacency list representation of the graph.
        
        Args:
            edges (list of lists): Each inner list contains two integers representing an edge.
            num_vertices (int): The total number of vertices in the graph.
        
        Returns:
            list of lists: Adjacency list where index represents the vertex and the list contains its neighbors.
        """
        # Initialize adjacency list for each vertex
        adjacency_list = [[] for _ in range(num_vertices)]
        
        # Populate adjacency list based on edges
        for edge in edges:
            vertex1, vertex2 = edge
            adjacency_list[vertex1].append(vertex2)
            adjacency_list[vertex2].append(vertex1)  # Undirected graph: add both directions
        
        return adjacency_list

    def depth_first_search(self, edges, num_vertices, source_vertex):
        """
        Perform Depth First Search (DFS) starting from the source vertex.
        
        Args:
            edges (list of lists): Each inner list contains two integers representing an edge.
            num_vertices (int): The total number of vertices in the graph.
            source_vertex (int): The starting vertex for DFS.
        
        Returns:
            list: List of vertices in the order they were visited during DFS.
        """
        # Build the graph from the edges
        graph = self.build_graph(edges, num_vertices)
        
        # Initialize stack for DFS traversal
        stack = deque()
        # Keep track of visited vertices
        visited = [False] * num_vertices
        # List to store the order of vertices visited
        dfs_result = []
        
        # Start DFS from the source vertex
        stack.append(source_vertex)

        while stack:
            # Pop the vertex from the stack
            current_vertex = stack.pop()
            
            # Process the vertex if it has not been visited
            if not visited[current_vertex]:
                dfs_result.append(current_vertex)
                visited[current_vertex] = True
                
                # Add all unvisited neighbors to the stack (reversed to maintain order)
                for neighbor in reversed(graph[current_vertex]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        return dfs_result

# Example usage
edges = [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 5], [3, 4], [3, 5]]
num_vertices = 6
source_vertex = 2

# Create an instance of the DepthFirstSearch class
dfs_instance = DepthFirstSearch()

# Perform DFS starting from the source vertex
dfs_result = dfs_instance.depth_first_search(edges, num_vertices, source_vertex)

# Print the DFS traversal order
for node in dfs_result:
    print(node, end=" ")

'''
Complexity Analysis:
- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
- Space Complexity: O(V + E), where V is the number of vertices and E is the number of edges, due to the adjacency list representation.
'''
