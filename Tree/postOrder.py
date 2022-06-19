class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class treeTraversal:

    def postOrder(self,root):
        n_root = root
        if n_root:
            self.postOrder(n_root.left)
            self.postOrder(n_root.right)
            print(n_root.data,end=" ")

    def iterativePostOrder(self,root):
        if not root: return
        curr = root
        prev = None
        stack = []
        while curr != None or stack:
            if curr != None:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack[-1]
                if curr.right == None or curr.right == prev:
                    stack.pop()
                    print(curr.data, end=" ")
                    prev = curr
                    curr = None
                else:
                    curr = curr.right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tt = treeTraversal()

print("\nPostorder traversal of binary tree is")
tt.postOrder(root)

print("\nIterativePostorder traversal of binary tree is")
tt.iterativePostOrder(root)
