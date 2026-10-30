class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}

        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1

            if i in cache:
                return cache[i]
            
            cache[i] = dfs(i-3) + dfs(i-2) + dfs(i-1)
            return cache[i]

        return dfs(n)

            