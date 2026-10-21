"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda interval: interval.start)   # sort by age


        temp = None

        rooms = 0

        # min heap of end times
        h =[]

        for interval in intervals:
            if not h:
                rooms += 1
                heapq.heappush(h, interval.end)
                continue

            if interval.start < h[0]:
                rooms += 1
                heapq.heappush(h, interval.end)
            else:
                heapq.heappop(h)
                heapq.heappush(h, interval.end)
            
        return rooms