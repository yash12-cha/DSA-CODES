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
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node

    # Reverse the linked list
    def reverseList(self):
        prev = None
        nxt = None
        curr = self.head
        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    # Helper method to add two linked lists
    def add(self,first,second):
        carry = 0
        ans = LinkedList()  # Initialize a new linked list to store the result
        while(first != None and second != None):
            sum = carry + first.data + second.data
            digit = sum%10
            ans.insert_at_end(digit)  # Add the digit to the result linked list
            carry = sum//10
            first = first.next
            second = second.next
        while (first != None):
            sum = carry + first.data
            digit = sum % 10
            ans.insert_at_end(digit)  # Add the digit to the result linked list
            carry = sum // 10
            first = first.next
        while(second != None):
            sum = carry + second.data
            digit = sum % 10
            ans.insert_at_end(digit)  # Add the digit to the result linked list
            carry = sum // 10
            second = second.next
        while (carry != 0):
            sum = carry
            digit = sum % 10
            ans.insert_at_end(digit)  # Add the digit to the result linked list
            carry = sum // 10
        return ans

    # Add two numbers represented by Linked List
    def addTwoLists(self,first,second):
        first.reverseList()  # Reverse the first linked list
        second.reverseList()  # Reverse the second linked list
        ans = self.add(first.head, second.head)  # Call the add method to perform addition
        ans.reverseList()  # Reverse the result to get the final answer
        return ans

    # Print (Traversal) the Linked list
    def print_LL(self):
        current = self.head
        if current == None:
            print("Linked List is empty!!!")
        else:
            while (current):
                print(current.data, end="--->")
                current = current.next
# First Linked List
head1 = LinkedList()
head1.insert_at_end(9)
head1.insert_at_end(9)
head1.insert_at_end(9)
head1.insert_at_end(9)
head1.insert_at_end(9)
head1.insert_at_end(9)
head1.insert_at_end(9)

# Second Linked List
head2 = LinkedList()
head2.insert_at_end(9)
head2.insert_at_end(9)
head2.insert_at_end(9)
head2.insert_at_end(9)

# Add two linked lists
result = head1.addTwoLists(head1, head2)

# Print the result
result.print_LL()

'''
Time Complexity: O(m + n)  where m and n are numbers of nodes in first and second lists respectively.
Space Complexity: O(m + n)  A temporary linked list is needed to store the output number.
'''
