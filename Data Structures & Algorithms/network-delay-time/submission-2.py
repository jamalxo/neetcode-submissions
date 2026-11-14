class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(len(times)):
            one, two, cost = times[i]
            adj.setdefault(one, []).append((two, cost)) 

        best = {}
        
        def dfs(node, time):
            if node in best and best[node] <= time:
                return
            best[node] = best.get(node, 1e9)
            best[node] = min(time, best[node])

            if node in adj:
                for nxt, w in adj[node]:
                    dfs(nxt, time + w)
        
        dfs(k, 0)
        
        return max(best.values()) if len(best) == n else -1