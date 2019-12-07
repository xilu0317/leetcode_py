# recursive
class Solution:
    def fib(self, N):
        if N == 0 or N == 1:
            return N

        if N == 2:
            return 1

        return self.fib(N - 1) + self.fib(N - 2)

# dp
class Solution2:
    def fib(self, n):
        if n == 0 or n == 1:
            return n

        if n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
