class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount+1)

        def dfs(left):
            if left == 0:
                return 0
            if cache[left] != -1:
                return cache[left]
            
            res = 1e9
            for c in coins:
                if left - c >= 0:
                    res = min(res, 1+ dfs(left-c))

            cache[left] = res
            return cache[left]

        res = dfs(amount)

        return res if res < 1e9 else -1
