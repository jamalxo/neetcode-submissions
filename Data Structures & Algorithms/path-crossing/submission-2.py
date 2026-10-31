class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moving = {'N': (1,0), 'S': (-1,0), 'W': (0,-1), 'E': (0,1)}

        seen = set()

        curr = (0,0)
        seen.add(curr)

        for c in path:
            move = moving[c]
            curr = (curr[0]+move[0], curr[1]+move[1])
            #print(moved)
            if curr in seen:
                return True
            seen.add(curr)
        
        return False