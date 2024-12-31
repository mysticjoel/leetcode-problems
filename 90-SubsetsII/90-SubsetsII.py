class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def findsub(ans, i):
            if i == len(nums):
                z.append(ans[:])
                return
            ans.append(nums[i])
            findsub(ans, i + 1)
            ans.pop()
            findsub(ans, i + 1)

        z = []
        findsub([], 0)
        #res = list(set(tuple(sorted(sub)) for sub in z))

        return list(set(tuple(sorted(sub)) for sub in z))
