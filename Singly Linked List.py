# Creation of node of Linked list
class Node:
    def __init__(self,data,next = None):
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
    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node

    # Insert new node at a specific position
    def add_pos(self, data,position):
        new_node = Node(data)

        # This condition to check whether the
        # position given is valid or not.
        if (position < 1):
            print("Invalid position!")

        # Linked List is empty
        if self.head == None:
            self.head = new_node

        # Insert at start
        if position == 1 :
            self.add_begin(data)
            return

        else:
            temp = self.head
            cnt = 1
            while(cnt < position - 1):
                temp = temp.next
                cnt += 1

            # Insert at end
            if(temp.next == None):
                self.add_end(data)
                return

            new_node.next = temp.next
            temp.next = new_node

    # Deletion of node in the beginning
    def delete_begin(self):
        if self.head == None:
            print("Linked List is empty can't delete!")
        else:
            self.head = self.head.next

    # Deletion of node at the end
    def delete_end(self):
        current = self.head
        if current == None:
            print("Linked List is empty can't delete!")
        elif current.next == None:
            current = None
        else:
            while (current.next.next):
                current = current.next
            current.next = None

    # Delete node from a specific position
    def delete_pos(self,position):
        # This condition to check whether the
        # position given is valid or not.
        if (position < 1):
            print("Invalid position!")

        if self.head == None:
            print("Linked List is empty can't delete!")

        # Delete from start
        if position == 1:
            self.delete_begin()
            return

        else:
            temp = self.head
            cnt = 1
            while(cnt < position - 1):
                temp = temp.next
                cnt += 1

            # Delete from end
            if(temp.next == None):
                self.delete_end()
                return

            temp.next = temp.next.next


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
LL.add_begin(5)
LL.add_end(6)
LL.add_pos(4,1)
LL.delete_begin()
LL.delete_end()
LL.delete_pos(3)
LL.print_LL()
