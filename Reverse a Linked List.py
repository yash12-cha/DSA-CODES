# Iterative Approach
def reverseList(self, head):
        prev = None
        curr = head
        while(curr):
            nextptr = curr.next
            curr.next = prev
            prev = curr
            curr  = nextptr
        head = prev
        return head
      
'''
Time Complexity: O(n), where n is the size of the linked list.
'''
