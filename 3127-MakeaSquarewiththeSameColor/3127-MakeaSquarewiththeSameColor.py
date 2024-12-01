class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        neighbour = [[0,0],[0,1],[1,0],[1,1]]
        for i in range(2):
            for j in range(2):
                w,b = 0,0
                for x,y in neighbour:
                    if grid[i+x][j+y]=='W':
                        w+=1
                    else:
                        b+=1
                    if b>=3 or w>=3:
                        #print(b,w)
                        return True
        return False

