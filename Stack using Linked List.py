# Stack using linked list

class Node:
    def __init__(self,key):
        self.data = key
        self.next = None
class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        if (self.root is None):
            return True
        return False
    def push(self,key):
        node = Node(key)
        node.next = self.root
        self.root = node
        print("The element is pushed and top points to => ", self.root.data)
    def pop(self):
        if (self.isEmpty()):
            print("Stack Underflow")
        else:
            poppednode = self.root.data
            self.root = self.root.next
            return poppednode
    def peek(self):
        if (self.isEmpty()):
            print("There is no record in the stack.")
            return -1
        else:
            return self.root.data

    def display(self):
        temp = self.root
        if (self.isEmpty()):
            print("There is no record in the stack.")
            return -1
        else:
            while(temp != None):
                print(temp.data,"->",end = " ")
                temp = temp.next

s = Stack()
while True:
    print("\nStack Operations")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch = int(input("Enter your choice (1-5): "))
    if ch == 1:
        x = int(input("Enter value: "))
        s.push(x)
    elif ch == 2:
        temp = s.pop()
        print("Popped element is: ", temp)
    elif ch == 3:
        print("Top element is: ", s.peek())
    elif ch == 4:
        s.display()
    elif ch == 5:
        break
    else:
        print("Please enter valid choice.")
