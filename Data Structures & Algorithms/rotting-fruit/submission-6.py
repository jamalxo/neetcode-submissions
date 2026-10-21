from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        self.fresh = 0

        def rotBanana(i, j):
            in_grid = i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])
            if in_grid and grid[i][j] == 1 and (i,j) not in visited:
                grid[i][j] = 2
                q.append((i,j))
                visited.add((i, j))
                self.fresh -= 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    self.fresh += 1

        minute = 0

        while q:
            for x in range(len(q)):
                i, j = q.popleft()
                rotBanana(i+1, j)
                rotBanana(i-1, j)
                rotBanana(i, j+1)
                rotBanana(i, j-1)
            if q:
                minute += 1

        return minute if self.fresh == 0 else -1