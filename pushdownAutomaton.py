# #
#
# Hugo Isaac Valdez Ruvalcaba - A01631301
#
# Program to validate parenthesis expresions
# Possible characters: (), [], {}
# 
# #

# Overrite index() function to return -1 if element not present in array
def indexOf(array, element):
    try:
        return array.index(element)
    except ValueError:
        return -1

# Evaluation function
def hasBalancedParenthesis(inputStr):
    stack = ['*']
    left = ['(','[','{']
    right = [')',']','}']
    for i in inputStr:
        if len(stack) == 1 or i in left:
            stack.append(i)
        elif i in right:
            peek = stack.pop()
            if indexOf(left, peek) != indexOf(right, i):
                stack.append(peek)
                stack.append(i)
    return stack.pop() == '*'

# Main
inputStr = '([(){}])()' # Adjust value to test 
print(hasBalancedParenthesis(inputStr))