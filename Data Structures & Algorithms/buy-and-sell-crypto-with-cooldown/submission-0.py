class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = [[-1] * 2 for _ in range(len(prices))]

        def dfs(i, holding):
            if i >= len(prices):
                return 0
            if cache[i][holding] != -1:
                return cache[i][holding]

            result = None
            
            if holding:
                sell = prices[i] + dfs(i+2, False)
                skip = dfs(i+1, True)
                result = max(sell, skip)
            else:
                buy = -prices[i] + dfs(i+1, True)
                skip = dfs(i+1, False)
                result = max(buy, skip)
            
            cache[i][holding] = result
            return cache[i][holding]

        
        xd =  dfs(0, False)
        print(cache)
        return xd