class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,time = 0,0
        rows,cols = len(grid),len(grid[0])
        queue = deque()
        #visit = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append([i,j])
        print(queue)
        print(fresh)
        n = [[0,1],[1,0],[0,-1],[-1,0]]
        while queue and fresh>0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in n:
                    row=dr+r
                    col = dc+c
                    if min(row,col)<0 or row==rows or col==cols or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    queue.append([row,col])
                    fresh-=1
                
            time+=1
        if fresh==0:
            return time
        else:
            return -1
        #return time