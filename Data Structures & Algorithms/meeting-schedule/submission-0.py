"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda interval: interval.start)   # sort by age

        res = True

        temp = None

        for interval in intervals:
            if not temp:
                temp = interval
                continue
            
            if temp.end > interval.start:
                res = False
            
            temp = interval
        
        return res