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

    # Reverse the linked list
    def reverseList(self):
        prev = None
        nxt = None
        curr = self.head
        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    # Print (Traversal) the Linked list
    def print_LL(self):
        current = self.head
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
print("Original List: ",end=" ")
LL.print_LL()
LL.reverseList()
print("\nReversed List: ",end= " ")
LL.print_LL()

'''
Output:
Original List:  1--->2--->3--->4--->5--->
Reversed List:  5--->4--->3--->2--->1--->
'''

'''
Time Complexity: O(n), where n is the size of the linked list.
'''
