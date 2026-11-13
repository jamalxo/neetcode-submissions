class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        if not amount:
            return 0
        def dfs(curr):
            if curr > amount:
                return 1e9
            if curr in cache:
                return cache[curr]
            if curr == amount:
                return 0
            res = 1e9
            for c in coins:
                res = min(1+dfs(curr+c), res)
            
            cache[curr] = res
            return res

        res = dfs(0)
        return res if res != 1e9 else -1