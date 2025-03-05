class Solution:
    def coloredCells(self, n: int) -> int:
        return n*n*2-2*n+1
        
        if n==1:return 1
        if n==2:return 5
        res=5
        k=3
        for _ in range(n-2):
            res+=2*(k-2)*2+4
            k+=1
        return res