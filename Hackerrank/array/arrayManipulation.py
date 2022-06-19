
def arrayManipulation(n, queries):
    arr = [0]*(n+2)
    for a,b,c in queries:
        arr[a] += c 
        arr[b+1] -= c 
    result = 0
    n_res = 0
    for v in arr:
        n_res += v 
        if n_res < 0:
            n_res = 0
        result = max(result,n_res)
    return result

q = [[1,2,100],[2,5,100],[3,4,100]]
print(arrayManipulation(5,q))
# 5 3
# 1 2 100
# 2 5 100
# 3 4 100