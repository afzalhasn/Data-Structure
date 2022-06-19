def expandFromMiddle(s,left,right):
    if left > right: return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longestPalindromeSubstr(s):
    n = len(s)
    if n < 1:return ''
    start = 0
    end = 0
    for i in range(n):
        l1 = expandFromMiddle(s,i,i)
        l2 = expandFromMiddle(s,i,i+1)
        l = max(l1, l2)
        if l > (end - start):
            start = i - (l-1)//2
            end = i + l//2
    return s[start:end+1]


s = 'forgeeksskeegfor'
s = 'racecaa'
print(longestPalindromeSubstr(s))
