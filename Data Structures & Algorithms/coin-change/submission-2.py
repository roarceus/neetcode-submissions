class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down (Memoization)
        # memo = {}

        # def dfs(amount):
        #     if amount == 0:
        #         return 0
        #     if amount in memo:
        #         return memo[amount]

        #     result = 1e9
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             result = min(result, 1 + dfs(amount - coin))

        #     memo[amount] = result
        #     return result

        # minCoins = dfs(amount)
        # return -1 if minCoins >= 1e9 else minCoins

        # Bottom Up (Tabulation)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1