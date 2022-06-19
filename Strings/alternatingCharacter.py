def alternatingCharacters(s):
    # Write your code here
    c = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            c += 1
    return c

print("AAAA")
print("BBBBB")
print("ABABABAB")
print("BABABA")
print("AAABBB")