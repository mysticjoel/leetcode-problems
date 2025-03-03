class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        mid = []
        right = []
        for i in nums:
            if i==pivot:
                mid.append(i)
            elif i<pivot:
                left.append(i)
            else:
                right.append(i)
        #left.sort(reverse=True)
        #right.sort()
        return left+mid+right