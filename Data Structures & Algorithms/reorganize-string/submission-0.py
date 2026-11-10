class Solution:
    def reorganizeString(self, s: str) -> str:
        #create max heap
        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i], 0) - 1
        h = []
        for k, v in counter.items():
            heapq.heappush(h, (v, k))

        res = []
        prev = None

        while h:
            print(h)
            amount, char = heapq.heappop(h)
            res.append(char)
                
            print(prev, amount)
            if prev:
                heapq.heappush(h, prev)
                prev = None
            if amount+1 < 0:
                new = (amount+1, char)
                prev = new
        
        return "".join(res) if len(res) == len(s) else ""