class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        union_find, i = UnionFind(m * n), 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    if c < n - 1 and grid[r][c + 1]:
                        union_find.merge(i, i + 1)
                    if r < m - 1 and grid[r + 1][c]:
                        union_find.merge(i, i + n)
                i += 1
        
        component_sums, i = defaultdict(int), 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    component_sums[union_find.find(i)] += grid[r][c]
                i += 1
        return max(component_sums.values(), default=0)

class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
    
    def find(self, i):
        if self.parents[i] != i: self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def merge(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri != rj:
            if self.ranks[ri] == self.ranks[rj]:
                self.parents[ri] = rj
                self.ranks[rj] += 1
            elif self.ranks[ri] < self.ranks[rj]:
                self.parents[ri] = rj
            else:
                self.parents[rj] = ri