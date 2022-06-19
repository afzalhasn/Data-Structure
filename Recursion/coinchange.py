def coinChange(t_sum,coin_arr,l,dp={}):
    if t_sum == 0:
        dp[l,t_sum] = 1
        return 1
    if t_sum < 0:
        dp[l,t_sum] = 0
        return 0
    if t_sum >= 1 and l<=0:
        dp[l,t_sum] = 0
        return 0
    if (l,t_sum) in dp:
        return dp[l,t_sum]
    dp[l,t_sum] = coinChange(t_sum-coin_arr[l-1],coin_arr,l,dp) + coinChange(t_sum,coin_arr,l-1,dp)
    return dp[l,t_sum]

coin_arr = [1,2,3]
t_sum = 4
n = 3
print(coinChange(t_sum,coin_arr,n))
