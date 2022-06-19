
def reverse(head):
    prev = None
    next_node = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverse_rec1(head):
    if not head or not head.next:
        return head
    if head.next:
        n_head = reverse_rec1(head.next)
        head.next.next = head
        head.next = None
    head.next = None
    return n_head
