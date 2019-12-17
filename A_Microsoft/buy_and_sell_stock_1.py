class Solution:
    def max_profit(self, prices):
        min_, max_profit = float('inf'), -float('inf')

        for x in prices:
            min_ = min(min_, x)
            max_profit = max(max_profit, x - min_)

        return max_profit if max_profit > 0 else 0
