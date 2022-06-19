def weirdStock(n, m):
    res = 0
    while(n < m):
        if m&1:
            m = m+1
        else:
            m = m//2
        res += 1
    return res + (n - m)

print(weirdStock(10,1))
