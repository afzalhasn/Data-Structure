def check_cycle(head):
    slow,fast = head,head
    while slow or fast:
        if slow.next == None or fast.next == None or fast.next.next == None:
            return False 
        slow = slow.next 
        fast = fast.next.next
        if slow == fast:
            return True
