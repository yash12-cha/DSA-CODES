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
    # Insertion of new node at the nth position
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
    # Deletion of node in the beginning
    def delete_begin(self):
        if self.head == None:
            print("Linked List is empty can't delete!")
        else:
            p = self.head=self.head.next
            return p
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
    # Deletion of node from nth position
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
while True:
    print("\nLinked List Operations:-")
    print("1. Insert at the beginning.")
    print("2. Insert at the end.")
    print("3. Delete from beginning.")
    print("4. Delete from end.")
    print("5. Display Linked List.")
    print("6. Exit.")
    print("\n")
    ch = int(input("Enter your choice (1-4): "))
    if ch == 1:
        x = int(input("Enter value to be inserted: "))
        LL.add_begin(x)
        print(x,"inserted successfully.\n")
    elif ch == 2:
        y = int(input("Enter value to be inserted: "))
        LL.add_end(y)
        print(y,"inserted successfully.\n")
    elif ch == 3:
        p = LL.delete_begin()
        print(p,"deleted successfully.")
    elif ch == 4:
        LL.delete_end()
    elif ch == 5:
        LL.print_LL()
    elif ch == 6:
        break
    else:
        print("Please enter valid choice!!!")
    
