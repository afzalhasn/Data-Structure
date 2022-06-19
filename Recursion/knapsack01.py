# 0/1 problem

def knapsack(weight_arr, value_arr,t_weight,n):
    if n==0 or t_weight==0:
        return 0
    if weight_arr[n-1] <= t_weight:
        return max(value_arr[n-1] + knapsack(weight_arr,value_arr,t_weight-weight_arr[n-1], n-1), knapsack(weight_arr,value_arr,t_weight,n-1 ))
    else:
        return knapsack(weight_arr,value_arr,t_weight,n-1 )

weight_arr = [2,3]
value_arr = [3,5]
t_weight = 10
n = 2
print(knapsack(weight_arr,value_arr,t_weight,n))
