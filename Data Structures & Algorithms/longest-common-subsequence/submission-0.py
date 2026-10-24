class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[-1] * len(text2) for _ in range(len(text1))]

        print(cache)

        # text 1 is our i 
        # text 2 is our j

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if cache[i][j] != -1:
                return cache[i][j]
            
            result = None
            if text1[i] == text2[j]:
                result =  1 + dfs(i + 1, j + 1)
            else:
                result = max(dfs(i +1, j), dfs(i, j+1))
            cache[i][j] = result
            return cache[i][j]

        result = dfs(0, 0)
        print(cache)
        return result