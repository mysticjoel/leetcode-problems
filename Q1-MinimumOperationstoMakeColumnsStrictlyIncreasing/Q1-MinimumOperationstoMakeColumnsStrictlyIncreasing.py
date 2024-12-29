class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        count = 0
        for j in range(len(grid[0])):
            for i in range(1,len(grid)):
                diff = grid[i-1][j] - grid[i][j]
                #print(diff)
                if diff>=0:
                    grid[i][j]+= (diff+1)
                    #print(grid[i-1][j],grid[i][j])
                    count+=(diff+1)
        return count