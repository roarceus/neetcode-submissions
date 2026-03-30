class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            # decision to include same number
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            # decision to not include same number and use next number
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return result