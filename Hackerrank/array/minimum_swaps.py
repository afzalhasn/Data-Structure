
def minimumSwaps(arr):
    i = 0
    swap = 0
    n = len(arr)
    while i < n:
        if arr[i] == i + 1:
            i += 1
        else:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            swap += 1
    return swap

arr = [2, 3, 4, 1, 5]
res = minimumSwaps(arr)
print(res)