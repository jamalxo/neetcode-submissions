class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        self.res = 0

        cache = {}

        def dfs(i, curr):
            if curr > amount or i >= len(coins):
                return 0
            
            if curr == amount:
                return 1

            if (i, curr) in cache:
                return cache[(i, curr)]
    
            # take
            take = dfs(i, curr+coins[i])

            # skip
            skip = dfs(i+1, curr)

            cache[(i, curr)] = take + skip

            return take + skip
    
            

        return dfs(0, 0)