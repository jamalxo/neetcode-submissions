class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)


        def dfs(i):
            print(cache)
            if i >= len(cost):
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]

        answer = min(dfs(0), dfs(1))


        return answer