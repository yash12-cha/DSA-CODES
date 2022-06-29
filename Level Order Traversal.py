                                    # Level Order Traversal of Binary Tree

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Defining class for the Binary Tree
class BinaryTreeTraversal:
    # Assigning root as null initially. So as soon as the object will be created
    # of this BinaryTreeTraversal class, root will be set as null.
    def __init__(self):
        self.root = None

    # Level Order Traversal
    def levelOrder(self,root):
        if root == None:
            return
        queue = deque()
        ans = []
        # Add root node to Queue
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.popleft()
            ans.append(node.data)
            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
        return ans




# Driver Code
tree = BinaryTreeTraversal()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print("Level Order Traversal is:", end=" ")
ans = tree.levelOrder(tree.root)
print(*ans)


# Time Complexity: O(n) , where n is the number of nodes in the binary tree.
