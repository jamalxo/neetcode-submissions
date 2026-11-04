class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.res = False
        odd_maybe = sum(matchsticks) / 4
        if not odd_maybe % 1 == 0:
            return False
        max_length = sum(matchsticks) // 4

        walking = {
            "U": 0,
            "D": 0,
            "L": 0,
            "R": 0,
        }

        matchsticks = sorted(matchsticks)
        matchsticks = matchsticks[::-1]

        def dfs(i):
            if i > len(matchsticks):
                return False
            for k,v in walking.items():
                if v > max_length:
                    return False
            if i == len(matchsticks):
                return walking["U"] == walking["D"] == walking["L"] == walking["R"]
            for k,v in walking.items():
                walking[k] += matchsticks[i]
                if dfs(i+1):
                    return True
                walking[k] -= matchsticks[i]
            
            return False


        return dfs(0)