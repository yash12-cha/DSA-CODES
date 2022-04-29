def reverseList(self, head):
        curr = head
        prev = None
        while(curr != None):
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        return prev
 '''
 Time Complexity: O(n) 
 '''
