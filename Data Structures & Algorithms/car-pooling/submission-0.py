class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # rearrange (start, end, cap)
        trips2 = []
        for i in range(len(trips)):
            trips2.append((trips[i][1], trips[i][2], trips[i][0]))
        trips = sorted(trips2)

        curr = capacity
        time = 0

        i = 0

        h = []

        while i < len(trips):
            while h and h[0][0] == time:
                end, amount = heapq.heappop(h)
                curr += amount

            while i < len(trips) and trips[i][0] == time:
                adding = (trips[i][1], trips[i][2])
                heapq.heappush(h, adding)
                curr -= trips[i][2]
                if curr < 0:
                    return False
                i+= 1
            
            time += 1
        
        return True