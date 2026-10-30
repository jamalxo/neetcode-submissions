class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.cache = {}

        def dfs(i, curr):
            if curr == t:
                return 1
            if len(curr) > len(t) or i >= len(s):
                return 0

            if (i,curr) in self.cache:
                return self.cache[(i,curr)]
            
            # take 
            take = dfs(i+1, curr+s[i])

            #skip
            skip = dfs(i+1, curr)

            self.cache[(i,curr)] = take+skip
            return self.cache[(i,curr)]
        
        return dfs(0, "")