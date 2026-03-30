class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        
        for k, v in hm.items():
            if v > len(nums) / 2:
                return k
        
        return 0