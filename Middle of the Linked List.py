# Creation of node of Linked list
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
# Join nodes to get a linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion of new node at the end
    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node

    # Function to get the middle of the linked list
    def middleNode(self):
        # Initialize two pointers
        slow = self.head
        fast = self.head
        # Iterate till fast is null and fast's next is null (fast reaches end)
        while (fast.next != None and fast!= None):
            slow = slow.next        # Move the slow pointer by one position
            fast = fast.next.next   # Move the fast pointer by two positions
        # return the slow's data, which would be the middle element.
        print("Middle node: ",slow.data)
        
LL = LinkedList()
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(5)
LL.middleNode()

'''
Output:
Middle node:  3
'''

'''
Time Complexity: O(N/2).
'''
