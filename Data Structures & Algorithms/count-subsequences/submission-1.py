class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.cache = {}

        def dfs(i, curr):
            #print(i, curr)
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
           #print("take,skeip" + str(take) + str(skip))

            self.cache[(i,curr)] = take+skip
            return self.cache[(i,curr)]
        
        return dfs(0, "")