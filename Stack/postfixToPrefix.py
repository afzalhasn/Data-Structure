
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

def postfixToPrefix(val):
    # operator + op2 + op1
    stack = []
    for v in val:
        if isOperand(v):
            stack.append(v)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(v+op2+op1)
    return stack.pop()

val = "ABC/-AK/L-*"
print(postfixToPrefix(val))
