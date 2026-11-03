class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)

        r = sum(weights)

        while l < r:
            mid = (l+r) // 2

            # is this capacity enough?
            curr_cap = mid
            daily_capacity = curr_cap
            i = 0
            curr_day = 1
            while i < len(weights):
                if weights[i] > curr_cap:        # this package can never ship
                    curr_day = float('inf')
                    break
                daily_capacity -= weights[i]
                if daily_capacity >= 0:
                    i += 1
                else:
                    curr_day += 1
                    daily_capacity = curr_cap - weights[i]
                    i+=1

            print(l, r, curr_day, mid)

            if curr_day <= days:
                r = mid
            else:
                l = mid +1
        
        return l
