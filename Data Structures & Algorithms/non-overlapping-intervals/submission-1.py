class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        res = []
        temp = None
        count = 0
        for interval in intervals:
            
            if not temp:
                temp = interval
                res.append(temp)
                continue
            
            if temp[1] > interval[0]:
                res.pop()
                mini = min(interval[1], temp[1])
                temp = [interval[0], mini]
                res.append(temp)
                count += 1
            else:
                res.append(interval)
                temp = interval
        
        return count