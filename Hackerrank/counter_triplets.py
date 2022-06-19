from collections import Counter

def countTriplets(arr, r):
    prev_counter = Counter()
    after_counter = Counter(arr)
    count = 0
    for a in arr:
        after_counter[a] -= 1
        if a%r == 0 and a//r in prev_counter and a*r in after_counter:
            count += prev_counter[a//r]*after_counter[a*r]
        prev_counter[a] += 1
    return count   

r = 5
arr = [1, 5, 5, 25, 125]
print(countTriplets(arr, r))
