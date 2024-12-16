class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            val=nums.index(min(nums))
            nums[val]*=multiplier
        return nums