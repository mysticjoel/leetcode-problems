class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        M = 1000000007
        nums.sort()
        tot=0
        pref = 0
        for x in range(len(nums)):
            tot+= (nums[x]**2) * (pref+nums[x])
            tot%=M
            pref = pref*2 + nums[x]
            pref%=M
        return tot