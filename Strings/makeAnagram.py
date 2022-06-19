def makeAnagram(a, b):
    # Write your code here
    c_a = Counter(a)
    c_b = Counter(b)
    count = 0
    for v in a:
        if not c_b[v]:
            count += 1
        if c_b[v] > 0:
            c_b[v] -= 1
    for v in b:
        if not c_a[v]:
            count += 1
        if c_a[v] > 0:
            c_a[v] -= 1
    return count

print(makeAnagram('cde', 'dcf'))
# delete minimum number of character from both string two make it anagram
