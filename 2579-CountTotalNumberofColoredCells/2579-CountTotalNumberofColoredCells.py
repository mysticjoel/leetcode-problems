class Solution:
    def coloredCells(self, n: int) -> int:
        c=1
        for i in range(n):
            c+=i*4
        return c