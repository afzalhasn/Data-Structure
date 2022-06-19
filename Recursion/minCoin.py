def minCoins(coins,n):
    table = [0] + [float('inf')]*n
    for coin in coins:
        for i in range(coin,n+1):
            table[i] = min(table[i], table[i-coin]+1)
    return table[n]
coins = [9,6,5,1]
V = 11
print(minCoins(coins,V))

# def minCoins(coins,m,V):
#     if V == 0:
#         return 0
#     res = float('inf')
#     for c in [coin for coin in coins if coin <= V]:
#         sub_res = minCoins(coins,m,V-c)
#         if sub_res != float('inf') and sub_res + 1 < res:
#             res = sub_res + 1
#     return res

# coins = [9,6,5,3]
# m = len(coins)
# V = 11
# print(minCoins(coins,m,V))