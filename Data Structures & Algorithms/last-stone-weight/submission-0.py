class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]

        heapq.heapify(h)

        while len(h) > 1:
            
            one = h[0]
            heapq.heappop(h)
            two = h[0]
            #print(h, one, two, -(abs(one) - abs(two)))


            if one == two:
                
                heapq.heappop(h)
            if two > one:
                
                heapq.heappop(h)
                heapq.heappush(h, -(abs(one) - abs(two)))
        #print(h)
        return -1 * h[0] if len(h) > 0 else 0