class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l = 1
        r = x

        prev = None

        while l <= r:
            mid = (l+r) // 2

            multi = mid * mid

            if multi == x:
                return mid
            elif multi > x:
                r = mid - 1
            else:
                l = mid + 1
        
        return l - 1