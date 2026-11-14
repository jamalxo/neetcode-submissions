class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        if len(text1) > len(text2):
            tmp = text1
            text1 = text2
            text2 = tmp

        cache = {}

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) in cache:
                return cache[(i,j)]
            
            res = 0
            if text1[i] == text2[j]:
                res =  1 + dfs(i+1, j+1)
            else:
                res = max(dfs(i, j+1), dfs(i+1, j))
            
            cache[(i,j)] = res

            return res


        return dfs(0,0)
