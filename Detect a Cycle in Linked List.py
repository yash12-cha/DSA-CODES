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

    # Detect cycle in linked list
    def hasCycle(self, head):
        slow = head
        fast = head
        if head == None:
            return False
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    # Print (Traversal) the Linked list
    def print_LL(self,head):
        current = head
        if current == None:
            print("Linked List is empty!!!")
        else:
            while (current):
                print(current.data, end="--->")
                current = current.next

LL = LinkedList()
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(5)
# Create a loop for testing
LL.head.next.next.next.next = LL.head.next
p = LL.hasCycle(LL.head)
if p == True:
    print("\nYes cycle is present in linked list.")
else:
    print("\nNo cycle is not present in linked list.")

'''
Output:
Yes cycle is present in linked list.
'''

'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
