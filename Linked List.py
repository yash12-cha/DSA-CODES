# Creation of node of Linked list
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
# Join nodes to get a linked list
class LinkedList:
    def __init__(self):
        self.head = None
    # Insertion of new node in the beginning
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # Insertion of new node at the end
    def add_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
    # Insertion of new node after the given node
    def after_node(self,data,x):
        current = self.head
        while(current):
            if x == current.data:
                break
            current = current.next
        if current == None:
            print("Node is not present in Linked List.")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
    # Insertion of new node before the given node
    def before_node(self,data,x):
        current = self.head
        if current == None:
            print("Linked List is empty.")
            return
        if current.data == x:
            new_node = Node(data)
            mew_node.next = current
            current = new_node
            return
        while(current):
            if current.next.data == x:
                break
            else:
                current = current.next
        if current.next == None:
            print("Node is not found!!!")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
    # Deletion of node in the beginning
    def delete_begin(self):
        if self.head == None:
            print("Linked List is empty can't delete!")
        else:
            self.head=self.head.next
    # Deletion of node at the end
    def delete_end(self):
        current = self.head
        if current == None:
            print("Linked List is empty can't delete!")
        elif current.next == None:
            current = None
        else:
            while(current.next.next):
                current = current.next
            current.next = None
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
LL.add_begin(5)
LL.add_begin(6)
LL.add_begin(7)
LL.add_end(15)
LL.after_node(20,6)
LL.before_node(23,6)
LL.delete_begin()
LL.delete_end()
LL.print_LL()
