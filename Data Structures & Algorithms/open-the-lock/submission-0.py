class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #bfs going to target if dead end reached dont go fruther there

        q = deque()

        init = "0000"

        q.append(init)

        seen = set()

        dead = set(deadends)

        steps = 0

        while q:
            for _ in range(len(q)):
                popped = q.popleft()
                if popped in seen:
                    continue
                seen.add(popped)
                if popped in dead:
                    continue

                # if final state return
                if popped == target:
                    return steps
                
                # up down for each
                for i in range(len(popped)):
                    up = popped[:i] + str((int(popped[i])+1) % 10) + popped[i+1:]
                    down = popped[:i] + str((int(popped[i])-1) % 10) + popped[i+1:]
                    q.append(up)  
                    q.append(down)   
            
            steps += 1

        return -1