class Solution:
    def maxScore(self, s: str) -> int:
        def findOne(s):
            c=0
            for i in s:
                if i=='1':
                    c+=1
            return c
        def findZero(s):
            c=0
            for i in s:
                if i=='0':
                    c+=1
            return c
        maxsum = 0
        for i in range(len(s)-1):
            left = s[0:i+1]
            right = s[i+1:len(s)]
            #print(left,right)
            cOne = findOne(right)
            cZero = findZero(left)
            #print(cOne,cZero)
            maxsum = max(cOne+cZero,maxsum)
            #maxzero = max(cZero,maxzero)
            #print(maxone,maxzero)
        return maxsum