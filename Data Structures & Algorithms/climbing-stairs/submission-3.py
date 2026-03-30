class Solution:
    def climbStairs(self, n: int) -> int:
        # Top Down (Memoization)
        # memo = { 0:1, 1:1 }

        # def f(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x] = f(x - 1) + f(x - 2)
        #         return memo[x]

        # return f(n)

        # Bottom Up (Tabulation)
        # if n <= 2:
        #     return n

        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]

        # Bottom Up (Tabulation) Space Optimized
        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one

        return one