def minimumBribes(q):
    # Write your code here
    count = 0
    for i in range(len(q)-1,-1,-1):
        if i+1 == q[i-2]:
            q[i-1],q[i-2] = q[i-2],q[i-1]
            q[i],q[i-1] = q[i-1],q[i]
            count += 2
        elif i+1 == q[i-1]:
            q[i],q[i-1] = q[i-1],q[i]
            count += 1
        elif i+1 == q[i]:
            continue
        else:
            print("Too chaotic")
            return
    print(count)
    return


# q = [2, 1, 5, 3, 4]
q = [2, 5, 1, 3, 4]
minimumBribes(q)
