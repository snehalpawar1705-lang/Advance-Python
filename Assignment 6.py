# Memorization method
# inputs
weights =  (2,1,3,2)
values = (12,10,20,15)
capacity = 5 

n = len(weights)

#Create memorization table
memo = [[-1]* (capacity + 1) for _ in range(n + 1)]

def knapsack(weights, values, n, capacity, memo)
    if n == 0 or capacity == 0:
        return 0

if memo[n][capacity] != -1:
    return memo[n][capacity]

if weights[n - 1] > capacity:
include = values[n - 1] + knapsack(
   weights,
   values,
   n - 1,
   capacity - weights[n - 1],
   memo
)
exclude = knapsack(
   weights,
   values,
   n - 1,
   capacity,
   memo
)
memo[n][capacity] = max(include, exclude)


#Find maximum value
result = knapsack(
    weights,
    values,
    n,
    capacity,
    memo
)

print("Maximum value:",result)




# Tabulation method
#Inputs
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

n = len(weights)

# Create DP table
dp = [[0] * (capacity + 1) for i in range(n + 1)]

# Fill the table
for i in range(1, n + 1):

    for w in range(1, capacity + 1):

        # Check if item can fit
        if weights[i - 1] <= w:

            # Take the item
            take = values[i - 1] + dp[i - 1][w - weights[i - 1]]

            # Don't take the item
            not_take = dp[i - 1][w]

            # Choose maximum
            dp[i][w] = max(take, not_take)

        else:
            # Item cannot fit
            dp[i][w] = dp[i - 1][w]


print("Maximum Value:", dp[n][capacity])
