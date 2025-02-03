class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxlen = 1
        inc = 1
        dec = 1
        for i in range(1,len(nums)):
            if nums[i-1]-nums[i]>0:
                dec+=1
                inc=1
            elif nums[i-1]-nums[i]<0:
                inc+=1
                dec=1
            else:
                inc=1
                dec=1
            curmax = max(inc,dec)
            if curmax>maxlen:
                maxlen = curmax
        return maxlen
            
            