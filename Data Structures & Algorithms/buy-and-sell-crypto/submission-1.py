class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        windowsize = 1
        maxreturn = 0

        while windowsize < len(prices):
            for i in range(0, len(prices)-windowsize):
                profit = prices[i+windowsize] - prices[i]

                if profit > maxreturn:
                    maxreturn = profit
            windowsize += 1
            
        return maxreturn
