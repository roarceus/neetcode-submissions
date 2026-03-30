class Solution:
    def binary_search(self, left: int, right: int, nums: List[int], target: int):
        if left > right:
            return -1
        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]

            if mid_num == target:
                return mid
            if mid_num < target:
                left = mid + 1
            if mid_num > target:
                right = mid - 1

        return self.binary_search(left, right, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)