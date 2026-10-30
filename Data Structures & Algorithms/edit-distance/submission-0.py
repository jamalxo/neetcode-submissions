class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.cache = {}

        def dfs(i,j):
            if i >= len(word1) and j >= len(word2):
                return 0
            if i >= len(word1):
                return len(word2) - j 
            if j >= len(word2):
                return len(word1) - i
            
            if (i,j) in self.cache:
                return self.cache[(i,j)]

            operations = 0

            if word1[i] == word2[j]:
                operations = dfs(i+1, j+1)
            else:
                #insert
                insert =  1 + dfs(i, j+1)
                #delete
                delete =  1 + dfs(i+1, j)
                #replace
                replace =  1 + dfs(i+1, j+1)

                operations = min(insert, delete, replace)
            
            self.cache[(i,j)] = operations
            return self.cache[(i,j)]

        return dfs(0,0)
        