class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## count tasks
        task_count = {}

        for task in tasks:
            task_count[task] = task_count.get(task, 0 ) + 1

        h = [(-value, key) for key, value in task_count.items()]

        heapq.heapify(h)
        q = deque()
        current_time = 0

        string = ""

        # maxheap and queue when to put back into heap
        while h or q:
            #print("pre", h , q, current_time)

            if q and q[0][1] == current_time:
                queue_pop = q.popleft()
                heapq.heappush(h, queue_pop[0])
            
            if h:
                popped = heapq.heappop(h)
                popped = (popped[0]+1, popped[1])          
                string += (popped[1])
                if popped[0] < 0:
                    q.append((popped, n+current_time+1))      
           
            current_time += 1
            

        return current_time