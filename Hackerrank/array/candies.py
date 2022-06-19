def candies(n, arr):
    # Write your code here
    arr1 = [1 for i in range(n)]
    arr2 = [1 for i in range(n)]
    res = 0
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            arr1[i] += arr1[i-1]
    for i in range(n-2,-1,-1):
        if arr[i] > arr[i+1]:
            arr2[i] += arr2[i+1]
    for i in range(n):
        res += max(arr1[i],arr2[i])
    print(res)

n = 10
arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
result = candies(n, arr)