# Stack Implementation using Array

class Stack:
    # We are assuming that the size of our stack is 5, you may take any size
    MAX = 5

    stack = []  # Stack

    # As soon as the object of this class is created, top is assigned as -1.
    def __init__(self):
        self.top = -1

    # It checks whether the stack is empty or not, obviously if top is -1, the stack will be empty.
    def isEmpty(self):
        if(self.top < 0):
            return True
        return False

    # It checks whether the stack is full or not, obviously if top is MAX - 1, the stack will be full.
    def isFull(self):
        if(self.top >= self.MAX - 1):
            return True
        return False

    # Function to push an element in the stack.
    def push(self,key):
        # if top becomes equal to MAX-1, then it means the array is full and we can't insert any element.
        # isFull() will return true, if stack is full.
        if(self.isFull()):
            print("Stack Overflow!!!")
            return False
        self.top += 1
        self.stack.append(key)
        print("The element is pushed and top points to => ", self.stack[self.top])
        return True

    # function to delete an element in the stack, it returns the deleted element otherwise -1. */
    def pop(self):
        # if top is -1, it means there is no element to be deleted
        if (self.isEmpty()):
            print("Stack Underflow!!!")
            return -1

        # otherwise, delete the element from the top and decrement top.
        deletedElement = self.stack[self.top]
        self.top -= 1
        return deletedElement

    # function through which we can see the element present at the top.
    def peek(self):
        if (self.isEmpty()):
            print("There is no record in the stack.")
            return -1

        peekElement = self.stack[self.top]
        return peekElement

    def display(self):
        if(self.isEmpty()):
            print("There is no record in the stack.")
            return -1
        else:
            for i in range(0,len(self.stack)):
                print(self.stack[i])
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
