class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a memo to store the results of subproblems
        memo = [float('inf')] * (amount + 1)

        # Set the base case: if the amount is 0, return 0
        memo[0] = 0

        # Iterate through the coins
        for coin in coins:
            # Iterate through the memo from left to right
            for i in range(coin, amount + 1):
                # Try including the current coin
                memo[i] = min(memo[i], memo[i - coin] + 1)

        # If the memo for the given amount is still infinity, return -1
        if memo[amount] == float('inf'):
            return -1

        # Return the result of the last subproblem
        return memo[amount]
