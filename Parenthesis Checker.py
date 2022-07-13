from collections import deque
def isValid(s):
    stack = deque()
    # Traversing the String
    for i in range(len(s)):
        # If the current character is a starting bracket(‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stack.append(s[i])
        else:
            # If current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if len(stack) == 0:
                return False
            # If the current character is a closing bracket(‘)’ or ‘}’ or ‘]’) then pop from stack and
            # if the popped character is the matching starting bracket then fine else brackets are not balanced
            current_char = stack.pop()
            if current_char == '(':
                if s[i] != ")":
                    return False
            if current_char == '{':
                if s[i] != "}":
                    return False
            if current_char == '[':
                if s[i] != "]":
                    return False
    # After complete traversal, if there is some starting bracket left in stack then “not balanced”
    if len(stack) != 0:
        return False
    else:
        return True
s = input("Input any string: ")
ans = isValid(s)
if ans == True:
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")

'''
Input any string: ()[]{}
Valid Parentheses

Time Complexity: O(n) 
Auxiliary Space: O(n) for stack. 
'''
