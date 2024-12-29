from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows,cols = len(maze),len(maze[0])
        queue = deque()
        queue.append(entrance)
        distance = 0
        visited = set()
        visited.add(tuple(entrance))
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and maze[r][c] == '.':
                    return distance
                for dr,dc in directions:
                    row = dr+r
                    col = dc+c
                    if row < 0 or col < 0 or row == rows or col == cols or maze[row][col] == '+' or (row, col) in visited:
                        continue
                    queue.append([row,col])
                    visited.add((row,col))
            distance+=1
        return -1
