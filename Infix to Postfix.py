# stack[-1] ---> used for accessing top element of the stack
# We can check whether the stack is empty or not using len(stack) if it is empty then it is 0 otherwise not

from collections import deque
# Function for precedence of operators
def prec(c):
        if c == '^':
            return 3
        elif c == '*' or c == '/':
            return 2
        elif c == '-' or c == '+':
            return 1
        # return -1 when not the operator
        else:
            return -1

class Solution:
    def InfixtoPostfix(self, exp):
        # Create empty stack
        stack = deque()
        # Output String
        output = ""
        for i in range(0,len(exp)):
            # isalpha() method returns True if all the characters are alphabet letters (a-z) or (A-Z)
            # Check if the charcater is operand
            if exp[i].isalpha():
                # if the character is operand add it to the output
                output += exp[i]
            # if character is '(' then push it directly to the stack
            elif exp[i] == '(':
                stack.append(exp[i])
            # if character is ')' then pop from stack until '(' is encountered or stack is empty
            elif exp[i] == ')':
                while (stack and stack[-1] != '('):
                    output+=stack.pop()
                # check whether stack is empty or not
                # if stack is not empty then pop the remaining elements
                if len(stack) !=0:
                    stack.pop()
            # An operator is encountered
            else:
                # check whether stack is empty or not 
                # and pop from stack until operator with less precedence is encountered
                while (len(stack) !=0 and prec(stack[-1]) >= prec(exp[i])):
                    output+=stack.pop()
                # add current operator to the stack
                stack.append(exp[i])
        # pop all the remaining items from the stack       
        while stack:
            output+=stack.pop()
        return output
