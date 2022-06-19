def getMaxDiff(A):
    n = len(A)
    if n == 0: return 0
    max_so_far = A[-1]
    diff = float('-inf')
    for i in range(n-1,-1,-1):
        if A[i] >= max_so_far:
            max_so_far = A[i]
        else:
            diff = max(diff, max_so_far - A[i])
    return diff


A = [2, 7, 9, 5, 1, 3, 5]
diff = getMaxDiff(A)
print(diff)