class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = 1
        zero = 0
        for i in nums:
            if i==0:
                zero+=1
            else:
                ans*=i
        res = [0] * len(nums)
        if(zero==1):
            res[nums.index(0)]=ans
            return res
        elif zero>1:
            return res
        else:
            for i in range(len(nums)):
                res[i] = ans//nums[i]
            return res