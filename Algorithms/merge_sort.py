"""
Input:
N = 10 
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 
1 2 3 4 5 6 7 8 9 10
"""
def merge(arr_1,arr_2):
    l_1 = len(arr_1)
    l_2 = len(arr_2)
    i1 = 0
    i2 = 0
    result = []
    while i1<l_1 and i2<l_2:
        if arr_1[i1] < arr_2[i2]:
            result.append(arr_1[i1])
            i1 += 1
        else:
            result.append(arr_2[i2])
            i2 += 1
    if i1 == l_1:
        result += arr_2[i2:]
    if i2 == l_2:
        result += arr_1[i1:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    sorted_1 = merge_sort(arr[:mid])
    sorted_2 = merge_sort(arr[mid:])
    return merge(sorted_1,sorted_2)

arr = [10,9,8,7,6,5,4,3,2,1]
n = 10
result = merge_sort(arr)
print(result)
