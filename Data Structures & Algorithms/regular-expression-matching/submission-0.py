class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.cache = {}

        def dfs(i,j):
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False

            if (i,j) in self.cache:
                return self.cache[(i,j)]

            match = i < len(s) and (s[i] == p[j] or p[j]== ".")

            # with star
            if j+1 < len(p) and p[j+1] == '*':
                #don't take or take star
                self.cache[(i,j)] =  dfs(i, j+2) or (match and dfs(i+1, j))
                return self.cache[(i,j)]
                
            if match:
                self.cache[(i,j)] =  dfs(i+1, j+1)
                return self.cache[(i,j)]
            
            self.cache[(i,j)] = False

            return self.cache[(i,j)]

        return dfs(0,0)
            