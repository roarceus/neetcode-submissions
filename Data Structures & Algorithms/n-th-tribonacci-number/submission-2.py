class Solution:
    # Top Down (Memoization)
    # def __init__(self):
    #     self.dp = {}

    def tribonacci(self, n: int) -> int:
        # Recursion
        # t = [0, 1, 1]
        # if n < 3:
        #     return t[n]
        # for i in range(3, n + 1):
        #     t[0], t[1], t[2] = t[1], t[2], sum(t)
        # return t[-1]

        # Top Down (Memoization)
        # if n <= 2:
        #     return 1 if n != 0 else 0
        # if n in self.dp:
        #     return self.dp[n]
        # self.dp[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        # return self.dp[n]

        # Bottom Up (Tabulation)
        if n <= 2:
            return 1 if n != 0 else 0
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]