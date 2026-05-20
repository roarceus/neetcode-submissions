class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Top Down (Memoization)
        # memo = [-1] * len(nums)

        # def dfs(i):
        #     if memo[i] != -1:
        #         return memo[i]

        #     LIS = 1
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS = max(LIS, 1 + dfs(j))

        #     memo[i] = LIS
        #     return LIS

        # return max(dfs(i) for i in range(len(nums)))

        # Bottom Up (Tabulation)
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)