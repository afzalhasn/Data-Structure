
def nth_to_last_node(val,s_node):
    count = 0
    curr_node = s_node
    while s_node:
        count += 1
        s_node = s_node.next
    res_node = count - val
    s = 0
    while curr_node:
        if s<res_node:
            s+=1
            curr_node = curr_node.next
            continue
        break
    return curr_node.data
