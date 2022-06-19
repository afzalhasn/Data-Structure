def fib_dyn(n):
    if cache[n] is not None:
        return cache[n]
    if n <=2:
        cache[n] = int((n+1)/2)
    else:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]

n = 10
cache = [None]*(n+1)

print(fib_dyn(n))
