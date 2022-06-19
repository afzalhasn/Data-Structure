
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

def prefixToInfix(val):
    # reverse
    # op1 + operator + op2
    stack = []
    for v in val[::-1]:
        if isOperand(v):
            stack.append(v)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append('('+op1+v+op2+')')
    return stack.pop()

val = "*+A/BC-/ADL"
print(prefixToInfix(val))
