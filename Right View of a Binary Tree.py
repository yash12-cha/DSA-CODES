class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def left_view_main(root,result,level,max_level):
    if root == None:
        return
    if level > max_level[0]:
        result.append(root.data)
        max_level[0] = level
    left_view_main(root.right, result, level + 1, max_level)
    left_view_main(root.left, result,level + 1, max_level)


def left_view(root):
    result = []
    max_level = [-1]
    left_view_main(root,result,0,max_level)
    return result

# Driver Code
root = Node(4)
root.left = Node(7)
root.right = Node(6)
root.right.left = Node(2)
root.right.left.left = Node(5)
root.right.left.right = Node(1)
root.right.left.right.left = Node(3)

print("Right View of Tree is:", end=" ")
left_view_result = left_view(root)
print(left_view_result)

'''
Time Complexity: The time complexity for above code is O(N), where N is the number of nodes in the binary tree. 
This is because we visit each node once during the traversal.

Space Complexity: O(N), due to the stack space during recursive call and the result list used. 
'''
