from collections import deque

class BreadthFirstSearch:
    def build_graph(self, edges, num_vertices):
        # Create an adjacency list for each vertex
        adjacency_list = [[] for _ in range(num_vertices)]
        
        # Populate the adjacency list with the given edges
        for edge in edges:
            vertex1, vertex2 = edge
            adjacency_list[vertex1].append(vertex2)
            adjacency_list[vertex2].append(vertex1)
        
        return adjacency_list

    def breadth_first_search(self, edges, num_vertices, source_vertex):
        # Build the graph from edges and vertices count
        graph = self.build_graph(edges, num_vertices)
        
        # Initialize the queue for BFS, the visited list, and the result list
        queue = deque()
        visited = [False] * num_vertices
        bfs_result = []

        # Start BFS from the source vertex
        queue.append(source_vertex)
        visited[source_vertex] = True

        while queue:
            # Dequeue a vertex from the front of the queue
            current_vertex = queue.popleft()
            bfs_result.append(current_vertex)

            # Enqueue all unvisited neighbors of the current vertex
            for neighbor in graph[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return bfs_result

# List of edges where each edge is represented as a pair of vertices
edges = [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 5], [3, 4], [3, 5]]

# Number of vertices in the graph
num_vertices = 6

# Source vertex for BFS
source_vertex = 0

# Create an instance of the BreadthFirstSearch class
bfs_instance = BreadthFirstSearch()

# Perform BFS starting from the source vertex
bfs_result = bfs_instance.breadth_first_search(edges, num_vertices, source_vertex)

# Print the BFS traversal order
for node in bfs_result:
    print(node, end=" ")

'''
Complexity Analysis
Time Complexity: O(V + E), where V is the number of nodes and E is the number of edges.

Space Complexity: 
O(V + E), where V is the number of nodes and E is the number of edges and this space is contributed by Adjacency List.
'''