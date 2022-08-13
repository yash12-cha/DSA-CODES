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
    def reverseList(self,head):
        if head == None or head.next == None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

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
print("Original List: ",end=" ")
LL.print_LL(LL.head)
p = LL.reverseList(LL.head)
print("\nReversed List: ",end= " ")
LL.print_LL(p)

'''
Output:
Original List:  1--->2--->3--->4--->5--->
Reversed List:  5--->4--->3--->2--->1--->
'''

'''
Time complexity: O(N), Where N is the size of the linked list.
'''
