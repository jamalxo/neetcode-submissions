class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [-1] * len(s)

        def dfs(i):
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if cache[i] != -1:
                return cache[i]

            if s[i] == '0':
                cache[i] = 0
                return 0
            
            ways = dfs(i+1)
            if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            cache[i] = ways
            return cache[i]


        return dfs(0)