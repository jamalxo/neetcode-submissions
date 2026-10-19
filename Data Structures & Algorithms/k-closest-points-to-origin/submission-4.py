import math

class Solution:
    def calc_distance(self, point):
        return math.sqrt(math.pow(point[0]-0, 2) + math.pow(point[1]-0, 2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tuples = [ (self.calc_distance(point), point[0], point[1]) for point in points]
        h = tuples
        heapq.heapify(h)
        
        res = []
        
        
        while h and k > 0:
            prev_tuple = heapq.heappop(h)
            prev = prev_tuple[0]
            res.append([prev_tuple[1], prev_tuple[2]])
            k += -1
            

        return res