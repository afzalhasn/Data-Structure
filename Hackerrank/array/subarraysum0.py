from collections import defaultdict
def count0(arr):
    d = defaultdict(list)
    s = 0
    for i,v in enumerate(arr):
        s += v 
        d[s].append(i)
    return d

arr = [15,-2,2,-8,1,7,10,23,-20,8,-29]
c = 0
for a,b in count0(arr).items():
    if a == 0:
        c += (len(b)*(len(b)+1))//2
    else:
        c += (len(b)*(len(b)-1))//2
print(c)