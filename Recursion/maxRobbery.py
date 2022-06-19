def maxRobbery(W, n, val, wt):
    dp = [0 for i in range(W + 1)]
    ans = 0
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
    return dp[W]

inp_array = list(map(int,input().split()))
# 10 3 5 2 3
t_weight = inp_array[0]
cost = inp_array[1:3]
weight = inp_array[3:]
print(maxRobbery(t_weight, 2, cost, weight))
