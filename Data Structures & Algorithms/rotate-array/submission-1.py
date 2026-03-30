class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        left, right = 0, len(nums) - 1
        self.swap(nums, left, right)

        left, right = 0, k - 1
        self.swap(nums, left, right)

        left, right = k, len(nums) - 1
        self.swap(nums, left, right)

    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1