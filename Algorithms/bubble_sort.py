"""
Input:
N = 10 
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 
1 2 3 4 5 6 7 8 9 10
"""
def bubble_sort(arr,n):
    for i in range(n):
        for j in range(1,n-i):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
    return arr

arr = [10,9,8,7,6,5,4,3,2,1]
n = 10
result = bubble_sort(arr,n)
print(result)
