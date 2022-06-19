
def bruteSearch(arr,start,end,val):
    if arr[start] >= val:
        return start
    elif arr[end-1] >= val:
        return end - 1
    elif arr[end] >= val:
        return end

def binarySearch(arr,start,end,val):
    if end - start == 0:
        return start
    if end - start <= 2:
        return bruteSearch(arr,start,end,val)
    mid = (start + end)//2
    if arr[mid] == val:
        return mid
    elif arr[mid] < val:
        return binarySearch(arr,mid,end,val)
    else:
        return binarySearch(arr,start,mid+1,val)

arr = [5,10,15,20,25]
print(binarySearch(arr,0,len(arr)-1,19))
