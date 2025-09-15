# Last updated: 9/15/2025, 2:19:06 PM
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.initial_nums = nums[:]
        self.nums = nums[:]
        
    def reset(self) -> List[int]:
        self.nums[:] = self.initial_nums[:]
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()