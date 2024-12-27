class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid)
        if grid[0][0]==1 or grid[rows-1][cols-1]:
            return -1
        queue = deque()
        visit = set()
        queue.append([0,0])
        visit.add((0,0))
        directions = [[0,1],[1,0],[1,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]
        length=1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                #print(r,c)
                if r==rows-1 and c==cols-1:
                    return length
                for dr,dc in directions:
                    row = dr+r
                    col = dc+c
                    #print(row,col)
                    if min(row,col)<0 or row==rows or col==cols or grid[row][col]==1 or (row,col) in visit:
                        continue
                    visit.add((row,col))
                    queue.append([row,col])
            length+=1
        return -1