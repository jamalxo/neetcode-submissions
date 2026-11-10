import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
    
        time = 0
        idle = True
        res = []
        h = []

        how_long = None

        new_tasks = []

        for i in range(len(tasks)):
            new = (tasks[i][0], tasks[i][1], i)
            new_tasks.append(new)

        tasks = sorted(new_tasks)
        i = 0

        while len(res) != len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(h, (tasks[i][1], tasks[i][2])) # time + index
                i+=1
            
            if h:
                time_task, index = heapq.heappop(h)
                res.append(index)
                idle = False
                time = time_task + time
            else:
                if i < len(tasks):
                    time = tasks[i][0]
                else:
                    time += 1
        
        return res