def sumArray(arr,n,k):
    s = 0
    d = {0:-1}
    maxlen = 0
    for i,a in enumerate(arr):
        s += a
        if s in d:
            maxlen = max(maxlen, i-d[s])
        else:
            d[s] = i
    return maxlen

def lenOfLongSubarr(arr, N, k) : 
    s = 0
    maxlen = 0
    mydict = {0:-1}
    i = 0
    for i in range(N):
        s += arr[i]
        if s not in mydict:
            mydict[s] = i
        if s-k in mydict:
            maxlen = max(maxlen, i-mydict[s-k])
    return maxlen

arr = [15,-2,2,-8,1,7,10,23]
print(sumArray(arr,len(arr),0))