
from collections import Counter

def sherlockAndAnagrams(s):
    m_set = Counter()
    for i in range(len(s)):
        for j in range(i,len(s)):
            v = ''.join(sorted(s[i:j+1]))
            m_set[v] += 1
    count = 0
    # for 3 same word it will make 3 combination (3*2)//2
    for k,v in m_set.items():
        count += v*(v-1)//2
    return count

print(sherlockAndAnagrams("abba"))
print(sherlockAndAnagrams("abcd"))
