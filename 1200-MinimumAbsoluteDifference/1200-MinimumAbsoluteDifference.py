class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        count = float('inf')
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])<count:
                count=abs(arr[i]-arr[i+1])
        
        minarr = []
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==count:
                minarr.append([arr[i],arr[i+1]])

        return minarr

