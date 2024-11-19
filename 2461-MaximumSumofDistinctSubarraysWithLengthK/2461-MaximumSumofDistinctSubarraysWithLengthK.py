class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        
        n = len(nums)
        s = set() # set to keep track of unique Numbers
        sumi = 0 # to track current window sum
        ans = 0 
        j = 0

        for i in range(n):
            
            while j<n and j-i < k and nums[j] not in s:
                sumi+=nums[j]
                s.add(nums[j])
                j+=1

            if j-i == k:
                ans = max(ans, sumi)

            s.remove(nums[i])
            sumi -= nums[i]

        return ans
                