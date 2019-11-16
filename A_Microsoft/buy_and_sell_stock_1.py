class Solution:
    def max_profit(self, prices):
        lowest_price, max_profit = float('inf'), -float('inf')

        for p in prices:
            lowest_price = min(lowest_price, p)
            max_profit = max(max_profit, p - lowest_price)

        return max_profit if max_profit > 0 else 0
