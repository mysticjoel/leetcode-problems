class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(len(nums)-1):
            prefix[i+1] = prefix[i]+nums[i+1]
        count = 0
        for i in range(len(nums)-1):
            start = prefix[i]
            end = prefix[-1] - prefix[i]
            #print(start,end)
            if start>=end:
                count+=1
#print(prefix)
        return count