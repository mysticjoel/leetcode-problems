class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        #totsum =  sum(grid[0])
        #print(totsum)
        prefix1 = [0]*len(grid[0])
        prefix2 = [0]*len(grid[0])
        prefix1[0] =  grid[0][0]
        prefix2[0] =  grid[1][0]
        for i in range(1,len(grid[0])):
            prefix1[i] = grid[0][i] + prefix1[i-1]
            prefix2[i] = grid[1][i] + prefix2[i-1]

        res = float('inf')
        for i in range(len(grid[0])):
            top = prefix1[-1] - prefix1[i]
            if i>0:
                bottom = prefix2[i-1]
            else:
                bottom = 0
            secondRobot = max(top,bottom)
            res = min(secondRobot,res)
        return res
            