from collections import deque


class Solution:
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()

        def addLand(i, j, depth):
            in_grid = i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])
            if in_grid and grid[i][j] > 0 and (i,j) not in visited:
                grid[i][j] = depth
                q.append((i,j))
                visited.add((i, j))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        print(q)

        depth = 0
        while q:
            depth += 1
            for item in range(len(q)):
                i, j = q.popleft()
                addLand(i+1, j, depth)
                addLand(i-1, j, depth)
                addLand(i, j+1, depth)
                addLand(i, j-1, depth)

                
                
                
                
                
        