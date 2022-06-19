
# time complexity O(2^n) exponential
def commonChild(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    if s1[m-1] == s2[n-1]:
        return 1 + commonChild(s1, s2, m-1, n-1)
    else:
        return max(commonChild(s1, s2, m-1, n) , commonChild(s1, s2, m, n-1))

# time complexity O(n*m)
def commonChild2(s1, s2, m, n, dp = {}):
    if m == 0 or n == 0:
        return 0
    if (m,n) in dp:
        return dp[m,n]
    if s1[m-1] == s2[n-1]:
        dp[m,n] = 1 + commonChild2(s1, s2, m-1, n-1)
    else:
        dp[m,n] = max(commonChild2(s1, s2, m-1, n) , commonChild2(s1, s2, m, n-1))
    return dp[m,n]

# time complexity O(n*m)
def commonChild3(s1, s2):
    l1, l2 = len(s1), len(s2)
    curr, prev = [0]*(l2+1), [0]*(l2+1)
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(prev[j], curr[j-1])
        curr, prev = prev, curr
    return prev[-1]

print(commonChild('acei','abcdefghi',4,9))
print(commonChild3('acei','abcdefghi'))



