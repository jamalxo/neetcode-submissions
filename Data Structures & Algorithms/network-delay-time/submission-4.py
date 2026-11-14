class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(len(times)):
            one, two, cost = times[i]
            adj.setdefault(one, []).append((two, cost)) 
        
        h = []
        heapq.heappush(h, (0, k))
        best = {}

        while h:
            w, node = heapq.heappop(h)
            if node in best:
                continue
            best[node] = w
            
            if node in adj:
                for nxt, w2 in adj[node]:
                    heapq.heappush(h, (w+w2, nxt))
            
        print(best)
        
        return max(best.values()) if len(best) == n else -1


