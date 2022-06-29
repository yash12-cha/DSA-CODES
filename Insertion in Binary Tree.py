                                    # Insertion in Binary Tree
# Time Complexity: O(n)

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeTraversal:

    def __init__(self):
        self.root = None

    # Insertion
    def insert(self,root,key):
        if root == None:
            return
        queue = deque()
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.popleft()
            if node.left == None:
                node.left = Node(key)
                break
            else:
                queue.append(node.left)
            if node.right == None:
                node.right = Node(key)
                break
            else:
                queue.append(node.right)

    # Inorder Traversal
    def InOrder(self,root):
        if root == None:
            return
        self.InOrder(root.left)
        print(root.data, end=" ")
        self.InOrder(root.right)



# Driver Code
tree = BinaryTreeTraversal()
tree.root = Node(10)
tree.root.left = Node(11)
tree.root.right = Node(9)
tree.root.left.left = Node(7)
tree.root.right.left = Node(15)
tree.root.right.right = Node(8)
print("Inorder Traversal before insertion: ",end= " ")
tree.InOrder(tree.root)
print()
key = 12
tree.insert(tree.root,key)
print("Inorder Traversal after insertion: ",end= " ")
tree.InOrder(tree.root)

