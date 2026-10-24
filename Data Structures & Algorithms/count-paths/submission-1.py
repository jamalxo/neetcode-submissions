class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(m)]

        print(cache)

        def outside(i, j):
            return i < 0 or j < 0 or i >= m or j >= n

        def end(i, j):
            return i == m-1 and j == n-1

        def dfs(i, j):
            if outside(i,j):
                return 0
            if end(i,j):
                return 1
            if cache[i][j] != -1:
                return cache[i][j]

            cache[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return cache[i][j]
        
        result = dfs(0,0)

        print(cache)
        return result