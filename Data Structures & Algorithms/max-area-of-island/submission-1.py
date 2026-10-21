class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.area = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0 
            if grid[i][j] == 1:
                
                grid[i][j] = -1
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j+1) +dfs(i, j-1)
            return 0
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or grid[i][j] == -1:
                    continue
                else:
                    # mark island with x
                    current = dfs(i, j)
                    
                    self.area = max(current, self.area)

        return self.area