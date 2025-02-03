class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        if nums[-1]-nums[0]>0:
            count+=1
        for i in range(len(nums)-1):
            #rint(nums[i+1]-nums[i])
            if nums[i+1]-nums[i]<0:
                #print(count)
                count+=1
            if count>1:
                return False
        return True