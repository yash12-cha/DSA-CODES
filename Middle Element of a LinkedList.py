# Creation of node of Linked list
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
# Join nodes to get a linked list
class LinkedList:
    def __init__(self):
        self.head = None
    # Insertion of new node 
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
    # Middle Element of a LinkedList
    def middle(self):
        current = self.head
        count = 0
        while(current):
            current = current.next
            count = count + 1
        current = self.head
        n = 0
        while(n < count / 2):
            current = current.next
            n = n + 1
        print(current.data)
    # Print the Linked list
    def print_LL(self):
        current = self.head
        if current == None:
            print("Linked List is empty!!!")
        else:
            while(current):
                print(current.data,end= "--->")
                current = current.next
LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(6)
LL.print_LL()
print("\n")
LL.middle()
