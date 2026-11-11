class Solution:
    def calc_n(self, i, j, grid):
        res = 0
        if i-1 < 0 or grid[i-1][j] == 0:
            res+=1
        if i+1 >= len(grid) or grid[i+1][j] == 0:
            res+=1
        if j-1 < 0 or grid[i][j-1] == 0:
            res+=1
        if j+1 >= len(grid[0]) or grid[i][j+1] == 0:
            res+=1
        
        return res
    
    def should_add(self, i, j, grid, seen):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and (i, j) not in seen and grid[i][j] == 1:
            seen.add((i,j))
            return True
        return False

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not q:
                    q.append((i,j))
                    seen.add((i, j))

        res = 0
        while q:
            i+=1
            for _ in range(len(q)):
                x, y = q.pop()
                res += self.calc_n(x,y,grid)
                if self.should_add(x+1, y, grid, seen):
                    q.append((x+1, y)) 
                if self.should_add(x-1, y, grid, seen):
                    q.append((x-1, y)) 
                if self.should_add(x, y+1, grid, seen):
                    q.append((x, y+1))
                if self.should_add(x, y-1, grid, seen):
                    q.append((x, y-1))
        
        return res

