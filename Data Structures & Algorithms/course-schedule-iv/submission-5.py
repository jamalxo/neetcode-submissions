class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(numCourses):
            adj.setdefault(i, [])
        for i in range(len(prerequisites)):
            pre, c = prerequisites[i][0], prerequisites[i][1]            
            adj[pre].append(c)
        res = [False for _ in range(len(queries))]
        #print(adj)
        def dfs(node, target, i):
            #print(node, target, i)
            if node in seen:
                return
            seen.add(node)
            if node == target:
                res[i] = True
                #print("setting")
                return
            neighbours = adj[node]
            for j in range(len(neighbours)):
                dfs(neighbours[j], target, i)
        
        for i in range(len(queries)):
            seen = set()
            dfs(queries[i][0], queries[i][1], i)

        return res
            
