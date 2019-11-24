# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1


class Solution:
    def coin_change(self, coins, amount):
        MAX = float('inf')

        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1, 1):
            for j in range(len(coins)):
                if (coins[j] <= i):
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[amount] > amount else dp[amount]
