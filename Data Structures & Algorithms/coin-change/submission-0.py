class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down (Memoization)
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            result = 1e9
            for c in coins:
                if amount - c >= 0:
                    result = min(result, 1 + dfs(amount - c))

            memo[amount] = result
            return result

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins