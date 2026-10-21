class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        res = []
        temp = None
        for interval in intervals:
            
            if not temp:
                temp = interval
                res.append(temp)
            
            if temp[1] >= interval[0]:
                res.pop()
                maxi = max(interval[1], temp[1])
                temp = [temp[0], maxi]
                res.append(temp)
            else:
                res.append(interval)
                temp = interval
        
        return res