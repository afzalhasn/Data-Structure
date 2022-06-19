
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

def postfixToInfix(val):
    # op2 + operator + op1
    stack = []
    for v in val:
        if isOperand(v):
            stack.append(v)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op2+v+op1)
    return stack.pop()

val = "ab*c+"
print(postfixToInfix(val))
