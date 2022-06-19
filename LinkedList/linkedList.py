from reversell import reverse, reverse_rec1
from nth_to_last_node import nth_to_last_node
from check_cycle import check_cycle

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self,val):
        if self.head == None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def printLL(self,start_node):
        while start_node:
            print(start_node.data)
            start_node = start_node.next

ll = LinkedList()
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.insert(9)
ll.insert(10)
print("Before reversing the linked list")
ll.printLL(ll.head)
# ----
# print("After reversing the linked list")
# n_node = reverse(ll.head)
# n_node = reverse_rec1(ll.head)
# ll.printLL(n_node)
# ----
# print(nth_to_last_node(3,ll.head))
# ----
# print(check_cycle(ll.head))
# ----

