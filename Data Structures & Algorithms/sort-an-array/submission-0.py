class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_two_sorted_lists(nums, left, right):
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

        def merge_sort(nums):
            if len(nums) <= 1:
                return

            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            merge_sort(left)
            merge_sort(right)

            merge_two_sorted_lists(nums, left, right)

        merge_sort(nums)
        return nums