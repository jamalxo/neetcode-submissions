class Solution:
    def outside(self, i,j, matrix):
        return i < 0 or 0 > j or i >= len(matrix) or j >= len(matrix[0])

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.cache = {}

        def dfs(i,j):
            if self.outside(i,j, matrix):
                return 0
                
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            
            # moving
            down = 0
            if not self.outside(i+1, j, matrix) and matrix[i+1][j] > matrix[i][j]:
                down = dfs(i+1,j)
            up = 0
            if not self.outside(i-1, j, matrix) and matrix[i-1][ j] > matrix[i][j]:
                up = dfs(i-1,j)
            right = 0
            if not self.outside(i, j+1, matrix) and matrix[i][ j+1] > matrix[i][j]:
                right = dfs(i,j+1)
            left = 0
            if not self.outside(i, j-1, matrix) and matrix[i][ j-1] > matrix[i][j]:
                left = dfs(i,j-1)

            maxi = 1 + max(down,up ,right , left)

            self.cache[(i, j)] = maxi

            return self.cache[(i, j)]
        
        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res
        

            
