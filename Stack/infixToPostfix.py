
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

def prec(x):
    if x == '^':
        return 3
    elif x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    return -1

def infixToPostfix(st):
    st_stack = []
    res = ''
    for a in st:
        if isOperand(a):
            res += a
        elif a == '(':
            st_stack.append(a)
        elif a == ')':
            while st_stack and st_stack[-1] != '(':
                res += st_stack.pop()
            if st_stack: st_stack.pop()
        else:
            while st_stack and prec(st_stack[-1]) >= prec(a):
                res += st_stack.pop()
            st_stack.append(a)
    while st_stack:
        res += st_stack.pop()
    return res

exp = "a+b*(c^d-e)^(f+g*h)-i"
print(infixToPostfix(exp))
