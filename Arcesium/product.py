def sign(n):
    if n>0:
        return 1
    else:
        return -1

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
    
    
first_negative = -1
last_negative = -1
flag = True
product = 1
for i in range(n):
    product = product*sign(lst[i])
    if lst[i]<0:
        last_negative = i
        if flag:
            first_negative = i
            flag = False
if product>0:
    print(n)
else:
    print(max(n-first_negative-1,last_negative))
