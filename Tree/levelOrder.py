class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class treeTraversal:
    
    def levelOrder(self,root):
        if not root: return
        stack = [root]
        result = []
        while stack:
            node = stack.pop(0)
            result.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tt = treeTraversal()

print("\levelOrder traversal of binary tree is")
print(tt.levelOrder(root))

