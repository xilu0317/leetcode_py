class Solution:
    def coin_change(self, coins, amount):
        dp = [0] + [float('inf')] * amount

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[amount] > amount else dp[amount]


class Solution:
    # [ISSUE] greedy: this ONLY works for nominal coins: 1, 5, 10, 50
    def coin_change(self, coins, amount):
        coins.sort()
        count, i = 0, len(coins) - 1

        while amount and i >= 0:
            if coins[i] <= amount:
                count += amount // coins[i]
                amount %= coins[i]
            i -= 1

        return -1 if amount > 0 else count
