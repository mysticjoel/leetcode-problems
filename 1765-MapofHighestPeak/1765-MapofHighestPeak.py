class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        output = isWater.copy()
        rows = len(isWater)
        cols = len(isWater[0])
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    output[i][j] = 0
                    queue.append([i,j])
                else:
                    output[i][j] = -1
        #print(output)
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            for i in range(len(queue)):
                r,c =  queue.popleft()
                for dr,dc in directions:
                    row = dr+r
                    col = dc+c
                    if min(row,col)<0 or row==rows or col==cols or output[row][col]!=-1:
                        continue
                    output[row][col] = output[r][c] + 1
                    queue.append([row,col])
        return output
