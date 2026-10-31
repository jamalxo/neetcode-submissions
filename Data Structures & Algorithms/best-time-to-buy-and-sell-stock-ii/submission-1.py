class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if (i, holding) in cache:
                return cache[(i,holding)]

            one = 0
            two = 0
            
            if holding:
                profit = prices[i] + dfs(i+1, False)
                cont = dfs(i+1, holding)
                one = max(profit, cont)
            # buy
            else:
                profit = -prices[i] + dfs(i+1, True)
                cont = dfs(i+1, holding)
                two = max(profit, cont)

            cache[(i,holding)] = max(one, two)

            return cache[(i,holding)]
    
        test =  dfs(0, False)
        print(cache)

        return test
        
            


            