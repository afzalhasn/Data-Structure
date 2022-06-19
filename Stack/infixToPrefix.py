from infixToPostfix import *

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

def infixToPrefix(st):
    # reverse string
    # infixtopostfix
    # reverse
    n_val = ''
    for v in st[::-1]:
        if v == ')':
            n_val += '('
        elif v == '(':
            n_val += ')'
        else:
            n_val += v
    return infixToPostfix(n_val)[::-1]

exp = "a+b*(c^d-e)^(f+g*h)-i"
print(infixToPrefix(exp))
