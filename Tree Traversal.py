                                    # Binary Tree Implementation and Traversal
# Time Complexity: O(n) , where n is the number of nodes in the binary tree.
# Create Node
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

    # Inorder Traversal
    def InOrder(self,root):
        if root == None:
            return
        self.InOrder(root.left)
        print(root.data, end=" ")
        self.InOrder(root.right)

    # Preorder Traversal
    def PreOrder(self,root):
        if root == None:
            return
        print(root.data, end=" ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    # Postorder Traversal
    def PostOrder(self,root):
        if root == None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.data, end=" ")

# Driver Code
tree = BinaryTreeTraversal()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print("Preorder Traversal is:", end=" ")
tree.PreOrder(tree.root)
print()
print("Inorder Traversal is:", end=" ")
tree.InOrder(tree.root)
print()
print("Postorder Traversal is:", end=" ")
tree.PostOrder(tree.root)
