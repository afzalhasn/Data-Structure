from collections import defaultdict, Counter
def checkSubstr(s,p):
    c_s = Counter(s)
    for s in p:
        if not c_s[s]:
            return False
    return True

def smallestWindow(s, p):
    st_s = defaultdict(list)
    for i,c in enumerate(s):
        st_s[c].append(i)
    for s_ind in st_s[p[0]][::-1]:
        for e_ind in st_s[p[-1]]:
            if s_ind > e_ind:
                continue
            n_str = s[s_ind:e_ind+1]
            if checkSubstr(n_str,p):
                return n_str
    return -1


S = "timetopractice"
P = "toc"
print(smallestWindow(S,P))
