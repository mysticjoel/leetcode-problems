def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
       n1, n2 = len(nums1), len(nums2)
       ans = 0
       if n2 % 2 == 1:
           for num1 in nums1:
               ans ^= num1
       if n1 % 2 == 1:
           for num2 in nums2:
               ans ^= num2
       return ans