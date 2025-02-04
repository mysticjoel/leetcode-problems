class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum = nums[0]
        curmax = nums[0]
        inc = 0
        for i in range(0,len(nums)-1):
            if nums[i+1]>nums[i]:
                maxsum+=nums[i+1]
            else:
                #curmax= max(maxsum,curmax)
                maxsum = nums[i+1]
            curmax= max(maxsum,curmax)
        return curmax
