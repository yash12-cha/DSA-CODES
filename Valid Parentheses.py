def isMatching(openingBracket, closingBracket):
	if(openingBracket == '{' and closingBracket == '}'):
		return True
	if(openingBracket == '(' and closingBracket == ')'):
		return True
	if(openingBracket == '[' and closingBracket == ']'):
		return True
	return False

def isValid(expression):
    stack = []
    for i in range(len(expression)):
        if(expression[i] == '{' or expression[i] == '(' or expression[i] == '['):
            stack.append(expression[i])
        else:
            if(len(stack) == 0):
                return False
            if(isMatching(stack.pop(), expression[i]) is not True):
                return False
    if(len(stack) == 0):
        return True
    return False

s = input()
check = isValid(s)
print(check)

'''
Input:-
()[]{}

Output:-
True
'''
