from collections import Counter

def isValid(s):
    s_count = Counter(s)
    s_val = sorted(s_count.values())
    len_s_val = len(s_val)
    return 'YES' if (s_val.count(s_val[0]) == len_s_val) or ((s_val.count(s_val[0])+1 == len_s_val) and (s_val[-1] - s_val[-2] == 1)) or ((s_val.count(s_val[-1])+1 == len_s_val) and (s_val[0] == 1)) else 'NO'


print(isValid('abcdefghhgfedecba'))


# [2, 2, 2]
# [2, 2, 2, 2, 3, 2, 2, 2]
# [2, 2, 2, 2, 1, 2, 2, 2]
# [2, 2, 2, 2, 1, 1, 2, 2, 2]
# [2, 2, 2, 2, 3, 3, 2, 2, 2]
