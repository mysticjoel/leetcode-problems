class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Mark walls as -1 and guards as 2
        for w in walls:
            grid[w[0]][w[1]] = -1
        for g in guards:
            grid[g[0]][g[1]] = 2

        for g in guards:
            for d in directions:
                x, y = g[0], g[1]
                while True:
                    x += d[0]
                    y += d[1]

                    # Stop if out of bounds or hits a wall/guard
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1 or grid[x][y] == 2:
                        break

                    # If unoccupied then mark
                    if grid[x][y] == 0:
                        grid[x][y] = 1

        # Count unguarded cells
        return sum(1 for i in range(m) for j in range(n) if grid[i][j] == 0)