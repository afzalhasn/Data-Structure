def possibleStrings(n, r, b, g):
    # code here 
    fact = [0 for i in range(n+1)]
    fact[0] = 1
    for i in range(1,n+1):
        fact[i] = fact[i-1]*i
    left = n - (r+g+b)
    summ = 0
    for i in range(left+1):
        for j in range(left-i+1):
            k = left - (i+j)
            summ = (summ + fact[n]//(fact[i+r]*fact[j+b]*fact[k+g]))
    return summ

n = 6
r = 1
g = 0
b = 1
print(possibleStrings(n,r,g,b))