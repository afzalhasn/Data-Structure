class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class treeTraversal:

    def preOrder(self,root):
        n_root = root
        if n_root:
            print(n_root.data,end=" ")
            self.preOrder(n_root.left)
            self.preOrder(n_root.right)

    def iterativePreOrder(self,root):
        if not root: return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tt = treeTraversal()
print("\nPreorder traversal of binary tree is")
tt.preOrder(root)

print("\nIterativePreorder traversal of binary tree is")
tt.iterativePreOrder(root)
