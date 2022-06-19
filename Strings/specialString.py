
def substrCount(n, s):
    i = 0
    result = 0
    while i < n:
        char_count = 1
        while i+1 < n and s[i] == s[i+1]:
            char_count += 1
            i += 1
        result += char_count*(char_count+1)//2
        i+=1
    for i in range(1,n):
        char_count = 1
        while (i+char_count < n and i - char_count >= 0) and s[i] != s[i-1] and s[i + char_count] == s[i - char_count] and s[i-char_count] == s[i-1]:
            char_count += 1
        result += char_count - 1
    return result
        
print(substrCount(4,'aaaa'))
print(substrCount(7,'abcbaba'))


# bbcbb



# abcbaba
# i = 1 
# if 