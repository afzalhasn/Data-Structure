def merge(arr0, arr1):
    inversions = 0
    result = []
    i0 = 0
    i1 = 0
    len0 = len(arr0)
    len1 = len(arr1)
    while len0 > i0 and len1 > i1:
        if arr0[i0] <= arr1[i1]:
            result.append(arr0[i0])
            i0 += 1
        else:
            # count the inversion right here: add the length of left array
            inversions += len0 - i0
            result.append(arr1[i1])
            i1 += 1

    if len0 == i0:
        result += arr1[i1:]
    elif len1 == i1:
        result += arr0[i0:]

    return result, inversions

def sort(arr):
    length = len(arr)
    mid = length//2
    if length >= 2:
        sorted_0, counts_0 = sort(arr[:mid])
        sorted_1, counts_1 = sort(arr[mid:])
        result, counts = merge(sorted_0, sorted_1)
        return result, counts + counts_0 + counts_1
    else:
        return arr, 0

def count_inversions(a):
    final_array, inversions = sort(a)
    return inversions
      
arr = [1, 20, 6, 4, 5]
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     arr = list(map(int, input().strip().split(' ')))
#     print(count_inversions(arr))
print(count_inversions(arr))
# Time Complexity: O(n log n)
# Space Complexity: O(n)
