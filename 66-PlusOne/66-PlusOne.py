class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = map(str,digits)
        num = ''.join(num)
        num = int(num)
        nums = num+1
        print(nums)
        new = list(map(int, str(nums)))
        return new