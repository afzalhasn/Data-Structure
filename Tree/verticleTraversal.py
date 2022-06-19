#         1
#       /   \ 
#      2     3
#     / \   / \
#    4   5 6   7
#           \   \
#            8   9

from collections import defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

class Traversal:
    def __init__(self):
        self.nodeinfo=defaultdict(list)
    def verticalTraversal(self,node,index):
        if node is None:
            return
        self.nodeinfo[index].append(node.data)
        if node.left:
            self.verticalTraversal(node.left,index-1)
        if node.right:
            self.verticalTraversal(node.right,index+1)

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.left = Node(6)
a.right.right = Node(7)
a.right.left.right = Node(8)
a.right.right.right = Node(9)
traversal = Traversal()
traversal.verticalTraversal(a,0)
for k,v in sorted(traversal.nodeinfo.items()):
    print(*v,end=' ')
