# Creation of node of Linked list
class Node:
    def __init__(self, data, next=None):
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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

def MergeLinkedLists(head1, head2):
    # A dummy node to store the result
    dummyNode = Node(0)
    p1 = head1
    p2 = head2
    p3 = dummyNode
    while (p1!=None and p2!= None):
        if (p1.data < p2.data):
            p3.next = p1
            p1 = p1.next
        else:
            p3.next = p2
            p2 = p2.next
        p3 = p3.next
    while(p1!=None):
        p3.next = p1
        p1 = p1.next
        p3 = p3.next
    while (p2 != None):
        p3.next = p2
        p2 = p2.next
        p3 = p3.next

    return dummyNode.next
LL1 = LinkedList()
LL1.add(1)
LL1.add(4)
LL1.add(5)
LL1.add(7)
LL2 = LinkedList()
LL2.add(2)
LL2.add(3)
LL2.add(6)
LL2.add(8)
LL1.head = MergeLinkedLists(LL1.head, LL2.head)
LL1.printList()

'''
Time Complexity: O(N + M), where N and M are the size of First LinkedList and Second LinkedList respectively.
Auxiliary Space: O(1)
'''
