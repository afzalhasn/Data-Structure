
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

def prefixToPostfix(val):
    # reverse
    # op1 + op2 + operator
    stack = []
    for v in val[::-1]:
        if isOperand(v):
            stack.append(v)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1+op2+v)
    return stack.pop()

val = "*-A/BC-/AKL"
print(prefixToPostfix(val))
