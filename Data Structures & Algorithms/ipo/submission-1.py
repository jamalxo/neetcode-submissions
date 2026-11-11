class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        trades = []
        for i in range(len(profits)):
            adding = (capital[i], profits[i])
            trades.append(adding)
        trades = sorted(trades)

        h = []
        res = 0

        i = 0

        while k > 0:
            while i < len(trades) and trades[i][0] <= w:
                heapq.heappush(h, -trades[i][1])
                i += 1
            
            #print(h, w)
            #print(h)
            if h:
                w += -heapq.heappop(h)
                k -= 1
            else:
                return w
        
        return w