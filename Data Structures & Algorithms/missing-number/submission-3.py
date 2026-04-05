class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sorting
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)

        # Hash set
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i