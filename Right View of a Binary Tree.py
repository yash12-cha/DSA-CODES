# Define a Node class for the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to find the right view of the binary tree
def right_view_main(root, result, level, max_level):
    if root is None:
        return
    if level > max_level[0]:
        # If this node is the rightmost node at the current level, add it to the result
        result.append(root.data)
        max_level[0] = level  # Update the maximum level seen so far
    # Traverse the right subtree before the left subtree to find the right view
    right_view_main(root.right, result, level + 1, max_level)
    right_view_main(root.left, result, level + 1, max_level)

def right_view(root):
    result = []       # Initialize an empty list to store the right view nodes
    max_level = [-1]  # Use a list to keep track of the maximum level seen (initialized to -1)
    
    # Call the right_view_main function to find the right view
    right_view_main(root, result, 0, max_level)
    
    return result

# Driver Code to create a binary tree
root = Node(4)
root.left = Node(7)
root.right = Node(6)
root.right.left = Node(2)
root.right.left.left = Node(5)
root.right.left.right = Node(1)
root.right.left.right.left = Node(3)

# Print the right view of the binary tree
print("Right View of Tree is:", end=" ")
right_view_result = right_view(root)
print(right_view_result)

'''
Time Complexity: The time complexity for above code is O(N), where N is the number of nodes in the binary tree. 
This is because we visit each node once during the traversal.

Space Complexity: O(N), due to the stack space during recursive call and the result list used. 
'''
