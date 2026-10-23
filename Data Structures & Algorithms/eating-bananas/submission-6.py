import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #binary search of speeds
        l = 1
        r = max(piles)
        close = 1
        while l < r:
            m = (l+r) // 2

            # can you finish?
            count = 0
            for pile in piles:
                count += math.ceil(pile / m)

            finish = count <= h
        
            if finish:
                r = m
            else:
                l = m +1
            if l == r:
                return l
        
        return close
