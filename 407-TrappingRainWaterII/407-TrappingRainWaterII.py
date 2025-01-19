import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M = len(heightMap)
        N = len(heightMap[0])

        # Hint BFS
        h = []


        for i in [0, M-1]:
            for j in range(N):
                h.append((heightMap[i][j], i, j))
                heightMap[i][j] = -1

        for i in range(1, M-1):
            for j in [0, N-1]: 
                h.append((heightMap[i][j], i, j))
                heightMap[i][j] = -1

        heapq.heapify(h)
  

        tot = 0
        while h:
            height, x, y = heapq.heappop(h)
            stack = [(x,y)]
            while h and h[0][0] == height:
                _, x, y = heapq.heappop(h)
                stack.append((x,y))
            while stack:
                x, y  = stack.pop()
                for d in [-1,1]:
                    nX = x + d
                    nY = y + d
                    if 0 > nX or M <= nX or heightMap[nX][y] == -1:
                        pass
                    else:
                        if height > heightMap[nX][y]:
                            tot +=  height - heightMap[nX][y]
                            stack.append((nX, y))
                            heightMap[nX][y] = -1
                        else:
                            heapq.heappush(h, (heightMap[nX][y], nX, y))
                            heightMap[nX][y] = -1
                        
                    if 0 > nY or N <= nY or heightMap[x][nY] == -1:
                        pass
                    else:
                        if height > heightMap[x][nY]:
                            tot += height - heightMap[x][nY]
                            stack.append((x, nY))
                            heightMap[x][nY] = -1
                        else:
                            heapq.heappush(h, (heightMap[x][nY], x, nY))
                            heightMap[x][nY] = -1

        return tot
