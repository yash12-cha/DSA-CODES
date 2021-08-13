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
    # Remove duplicates from a sorted linked list
    def remove(self):
        current = self.head
        while(current.next):
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
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
LL.insert(11)
LL.insert(11)
LL.insert(11)
LL.insert(21)
LL.insert(43)
LL.insert(43)
LL.insert(60)
LL.print_LL()
print("\n")
LL.remove()
LL.print_LL()
