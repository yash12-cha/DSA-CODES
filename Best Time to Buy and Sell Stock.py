def maxProfit(prices):
    # Get the length of the prices array
    n = len(prices)

    # Initialize variables to track the maximum profit and minimum price encountered so far
    max_profit = 0
    min_so_far = prices[0]

    # Iterate through the prices array
    for i in range(n):
        # Update the minimum price encountered so far
        min_so_far = min(min_so_far, prices[i])

        # Calculate the profit if we sell at the current price
        profit = prices[i] - min_so_far

        # Update the maximum profit if a better profit is found
        max_profit = max(max_profit, profit)

    # Return the maximum profit obtained
    return max_profit

# Get the input array of stock prices from the user
prices = list(map(int, input("Input Array: ").split()))

# Call the maxProfit function and store the result in the 'ans' variable
ans = maxProfit(prices)

# Print the maximum profit obtained
print("Maximum Profit:", ans)
