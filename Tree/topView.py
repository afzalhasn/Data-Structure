from collections import defaultdict

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def topView(root,t_dict = {},index=0,l=0):
    if root == None:
        return
    if index not in t_dict:
        t_dict[index] = [root.data,l]
    elif t_dict[index][1] > l:
        t_dict[index] = [root.data,l]
    topView(root.left,t_dict,index-1,l+1)
    topView(root.right,t_dict,index+1,l+1)
    return t_dict

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)

    # leftViewR(root)
    # print()
    # leftView(root)
    t_dict = {}
    results = topView2(root,t_dict)
    print(results)
    for k,v in sorted(results.items()):
        print(v[0],end=' ')
    # for k,v in sorted(topView(root).items()):
    #     print(v[0],end=' ')
