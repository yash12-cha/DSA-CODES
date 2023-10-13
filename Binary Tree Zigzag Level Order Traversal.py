from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTreeTraversal:
    def __init__(self):
        self.root = None

    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        currLevel = deque()
        nextLevel = deque()
        leftToRight = True
        ans = []

        currLevel.append(root)

        while len(currLevel) != 0:
            node = currLevel.pop()
            ans.append(node.data)  # Add the node's data to the result list.

            # Depending on the traversal direction, enqueue the left and right children.
            if leftToRight:
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)
            else:
                if node.right is not None:
                    nextLevel.append(node.right)
                if node.left is not None:
                    nextLevel.append(node.left)

            # When the current level is processed, switch the levels and reverse the direction.
            if len(currLevel) == 0:
                currLevel, nextLevel = nextLevel, currLevel  # Swap current and next levels.
                leftToRight = not leftToRight  # Change the traversal direction.

        return ans

# Driver Code
tree = BinaryTreeTraversal()
tree.root = Node(12)
tree.root.left = Node(9)
tree.root.right = Node(15)
tree.root.left.left = Node(5)
tree.root.left.right = Node(10)
print("Zigzag Level Order Traversal is:", end=" ")
ans = tree.zigzagLevelOrder(tree.root)
print(*ans)

'''
Time Complexity: O(N), where N is the number of nodes in the binary tree. 
Space Complexity: O(N), where N is the number of nodes in the binary tree. 
'''

