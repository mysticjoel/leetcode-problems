class Solution:
    def binarysearch(self,arr,k):
        left, right = 0, len(arr) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid]<k:
                left = mid + 1 
            elif arr[mid]>k:
                right = mid - 1
            else:
                return mid
        return -1

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        print(arr)
        for i in range(len(arr)):
            #print(arr[i]*2)
            res = self.binarysearch(arr,arr[i]*2)
            if i!=res and res!=-1:
                return True
        return False
            