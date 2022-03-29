def deleteNode(self, node):
        temp = node.next.val
        node.next = node.next.next
        node.val = temp
        
'''
Time Complexity: O(1)
'''
