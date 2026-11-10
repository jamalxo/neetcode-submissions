class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        h = []

        if a > 0:
            heapq.heappush(h, (-a, 'a'))
        if b > 0:
            heapq.heappush(h, (-b, 'b'))
        if c > 0:
            heapq.heappush(h, (-c, 'c'))

        bench = None

        res = []

        while h:
            print(h, bench)
            amount, char = heapq.heappop(h)
            res.append(char)
            amount = amount + 1
            
            if bench:
                heapq.heappush(h, bench)
                bench = None
            
            if amount < 0 and len(res) > 1 and res[-1] == char and res[-2] == char:
                bench = (amount, char)
            elif amount < 0:
                heapq.heappush(h, (amount, char))


        return "".join(res)