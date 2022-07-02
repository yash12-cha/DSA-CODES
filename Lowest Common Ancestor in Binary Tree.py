                                    # Lowest Common Ancestor in a Binary Tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeTraversal:

    def __init__(self):
        self.root = None


    def findLCA(self,root,n1,n2):
        # Base Case
        if root == None:
            return
        # If either n1 or n2 matches with root's data, report
        # the presence by returning root's data
        if root.data == n1 or root.data == n2:
            return root.data

        # Look for keys in left and right subtrees
        left_lca = self.findLCA(root.left, n1, n2)
        right_lca = self.findLCA(root.right, n1, n2)

        # If left subtree return NULL value, then return right subtree
        if left_lca == None:
            return right_lca
        # If right subtree return NULL value, then return left subtree
        if right_lca == None:
            return left_lca
        # If both left and right subtree return Non-NULL, then return root's data
        return root.data

# Driver Code
tree = BinaryTreeTraversal()
tree.root = Node(5)
tree.root.left = Node(4)
tree.root.right = Node(6)
tree.root.left.left = Node(3)
tree.root.right.right = Node(7)
tree.root.right.right.right= Node(8)
print ("LCA(7,8): ",tree.findLCA(tree.root,7,8))

# Time Complexity:  The time complexity of the above solution is O(n) as the method does a simple tree traversal in a bottom-up fashion. 
