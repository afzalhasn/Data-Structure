
from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def leftView(root):
    q = deque()
    q.append(root)
    while q:
        n = len(q)
        for i in range(n):
            temp = q.popleft()
            if i == 0:
                print(temp.data,end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

def leftViewR(root,level=1,last_level=0):
    if root is None: return last_level
    if last_level < level:
        print(root.data,end=' ')
        last_level = level
    last_level = leftViewR(root.left,level+1,last_level)
    last_level = leftViewR(root.right,level+1,last_level)
    return last_level

def leftViewR2(root):
    if root is None: return 
    print(root.data,end = ' ')
    if root.left:
        leftViewR2(root.left)
    if not root.left and root.right:
        leftViewR2(root.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)

    leftViewR2(root)
    print()
    leftView(root)
