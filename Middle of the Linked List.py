def middleNode(self, head):
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow
        
'''
Time Complexity: O(n), where n is the size of the linked list.
'''
 
