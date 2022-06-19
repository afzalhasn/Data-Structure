from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def rightView(root):
    q = deque()
    q.append(root)
    while q:
        n = len(q)
        for i in range(n):
            temp = q.popleft()
            if i == 0:
                print(temp.data,end=" ")
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    rightView(root)
