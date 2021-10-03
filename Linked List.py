# Linked List Implementation using Python

# Creation of node of Linked list
class Node:
    def __init__(self,data):
        self.data = data
        self. next = None
        
# Join nodes to get a linked list
class LinkedList():
    def __init__(self):
        self.head = None
        
     # Insertion of new node in the beginning
    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insertion of new node at the end
    def insert_end(self,data):
        new_node= Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
    
    # Insertion of new node at the nth position
    def insert_nth(self,data,position):
        new_node = Node(data)
        temp = self.head
        counter = 0
        while(temp.next):
            if counter == position:
                new_node.next = temp.next
                temp.next = new_node
                break
            counter = counter + 1
            temp = temp.next
        
    # Deletion of node in the beginning
    def delete_begin(self):
        if self.head == None:
            print("Linked List is empty can't delete!")
        else:
            p = self.head.data
            self.head=self.head.next
            return p
    
    # Deletion of node in the end
    def delete_end(self,position):
        if self.head == None:
            print("Linked List is empty can't delete!")
        elif self.head.next == None:
            self.head = None
        else:
            temp = self.head
            while(temp.next.next):
                temp = temp.next
            p = temp.next.data
            temp.next = None
        return p
              
    # # Deletion of node at the nth position 
    # def delete_nth(self,position):
    #     if self.head == None:
    #         print("Linked List is empty can't delete!")
    #     else:
    #         temp = self.head
    #         counter = 0
    #         while(temp.next):
    #             if counter == position:
    #                 # p = temp.next.data
    #                 temp
    #                 temp.next = None
    #                 break
    #             counter = counter + 1
    #             temp = temp.next
    #     # return p                
    # Print the Linked list
    def display(self):
        if self.head == None:
            print("Linked List is Empty!!!")
        else:
            temp = self.head
            while temp != None:
                print(temp.data,end= "--->")
                temp = temp.next
linked_list = LinkedList()
while True:
    print("\nLinked List Operations")
    print("1. Insert At The Beginning")
    print("2. Insert At The End")
    print("3. Insert At The nth position")
    print("4. Delete from beginning.")
    print("5. Delete from end.")
    # print("6. Delete At The nth position")
    print("7. Display")
    print("8. Exit")
    print("\n")
    ch = int(input("Enter your choice (1-8): "))
    if ch == 1:
        x = int(input("Enter value: "))
        linked_list.insert_begin(x)
        print(x,"inserted successfully.")
    elif ch == 2:
        x = int(input("Enter value: "))
        linked_list.insert_end(x)
        print(x,"inserted successfully.")
    elif ch == 3:
        x = int(input("Enter value: "))
        y = int(input("Enter position: "))
        linked_list.insert_nth(x,y)
        print(x,"inserted successfully at position",y)
    elif ch == 4:
        p = linked_list.delete_begin()
        print(p,"deleted successfully.")
    elif ch == 5:
        p = linked_list.delete_end()
        print(p,"deleted successfully.")
    # elif ch == 6:
    #     y = int(input("Enter position: "))
    #     linked_list.delete_nth(y)
    #     # print(p,"deleted successfully from position",y)
    elif ch == 7:
        linked_list.display()
    elif ch == 8:
        break
    else:
        print("Please enter valid choice.")

    
