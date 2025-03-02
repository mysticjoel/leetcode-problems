class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        new =  nums1+nums2
        new.sort(key=lambda x: x[0])
        res = []
        i=0
        while i<len(new):
            if i+1!=len(new) and new[i][0]==new[i+1][0]:
                res.append([new[i][0],new[i][1] + new[i+1][1]])
                i+=2
            else:
                res.append(new[i])
                i+=1
        return res