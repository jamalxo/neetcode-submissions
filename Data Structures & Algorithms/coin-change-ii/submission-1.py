class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        if amount == 0:
            return 1

        cache = [[-1] * (amount+1) for _ in range(len(coins))]

        def dfs(coin, curr):
            if curr > amount:
                return 0
            if curr == amount:
                return 1
            if coin == len(coins):
                return 0 
            if cache[coin][curr] != -1:
                return cache[coin][curr]

            result = None

            take = dfs(coin, curr + coins[coin])   # use this coin again
            skip = dfs(coin + 1, curr)  
            
            cache[coin][curr] = take + skip
            return cache[coin][curr]

        for i in range(len(coins)):
            dfs(i, 0)
        
        return cache[0][0]