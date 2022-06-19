# Find maximum profit earned by buying and selling shares any number of times

def findMaxProfit(price):
    n = len(price)
    profit = 0 
    j = 0

    for i in range(1,n):
        print(i,profit)
        if price[i-1] > price[i]:
            j = i
        
        if price[i-1] <= price[i] and ( i+1 == n or price[i] > price[i+1]):
            profit += price[i] - price[j]
    return profit



price = [1, 5, 2, 3, 7, 6, 4, 5]
print("\nTotal profit earned is", findMaxProfit(price))