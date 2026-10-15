class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 1
        while l < r:
            mid = (l + r) // 2

            total = sum(math.ceil(p / mid) for p in piles)            
            
            if total <= h:
                r = mid
            else:
                l = mid + 1

            if l == r:
                res = l
        
        return res