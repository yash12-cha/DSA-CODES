class AdjacencyList:
    def build_graph(self, edges, number_of_vertices):
        adjacency_list = []
        # Create an empty adjacency list for each vertex
        for _ in range(number_of_vertices):
            adjacency_list.append([])
        # Populate the adjacency list with the given edges
        for edge in edges:
            vertex1, vertex2 = edge
            adjacency_list[vertex1].append(vertex2)
            adjacency_list[vertex2].append(vertex1)
        
        return adjacency_list

# List of edges where each edge is represented as a pair of vertices
edges = [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 5], [3, 4], [3, 5]]

# Number of vertices in the graph
number_of_vertices = 6

# Create an instance of the AdjacencyList class
adjacency_list_instance = AdjacencyList()

# Build the graph using the adjacency list representation
graph = adjacency_list_instance.build_graph(edges, number_of_vertices)

# Print the adjacency list
for vertex in range(number_of_vertices):
    print(vertex, end=" : ")
    for neighbor in graph[vertex]:
        print(neighbor, end=" ")
    print()

'''
Complexity Analysis
Time Complexity:
O(V + E), where V is the number of vertex and E is the number of edges. In the worst-case scenario, each node can be connected to every other node. Therefore, the total number of edges would be V2 and hence in such a case, we can say that the Time Complexity would be O(V2).

Space Complexity:
O(V + E), where V is the number of vertex and E is the number of edges. This space is contributed by Adjacency List.
'''