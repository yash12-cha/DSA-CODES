from collections import deque

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, s):
        # Create an empty stack
        stack = deque()
        # scan the expression from left to right
        for i in range(0,len(s)):
            # check if the character encountered is an operand or not
            if (s[i]>= '0' and s[i] <= '9'):
                # convert the character to integer and add it to the stack
                stack.append(int(s[i]))
            # if the character encountered is an operator
            else:
                # pop the top operand from the stack and store it in a variable op2
                op2 = stack[-1]
                stack.pop() 
                # pop the top operand from the stack and store it in a variable op1
                op1 = stack[-1]
                stack.pop()
                # perform the required operation on the operands and push the result back to the stack
                if s[i] == '+':
                    stack.append(op1+op2)
                elif s[i] == '-':
                    stack.append(op1-op2)
                elif s[i] == '*':
                    stack.append(op1*op2)
                elif s[i] == '/':
                    stack.append(op1//op2)
                elif s[i] == '^':
                    stack.append(op1**op2)
        # When the expression is ended, the item in the stack is the final result so, return the top element of the stack
        return stack[-1]
