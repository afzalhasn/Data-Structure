class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class treeTraversal:
    
    def iterativeInOrder(self,root):
        if not root: return
        stack = []
        result = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack: break
                root = stack.pop()
                result.append(root.data)
                root = root.right
        print(*result)

    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.data,end=" ")
            self.inOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tt = treeTraversal()

print("\nInorder traversal of binary tree is")
tt.inOrder(root)

print("\nIterativeInorder traversal of binary tree is")
tt.iterativeInOrder(root)
