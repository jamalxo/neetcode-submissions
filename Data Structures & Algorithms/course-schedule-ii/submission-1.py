class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c_p = {}
        in_degree = [0]*numCourses


        for i in range(numCourses):
            c_p.setdefault(i, [])

        for course, pre in prerequisites:
            c_p[pre].append(course)
            in_degree[course] += 1
        
        starting = []

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                starting.append(i)

        res = []

        def dfs(course):
            if in_degree[course] == 0:
                res.append(course)
                for pres in c_p[course]:
                    in_degree[pres] -= 1
                    if in_degree[pres] == 0:
                        dfs(pres)

        for s in starting:
            dfs(s)
        print(res)
        return res if len(res) == numCourses else []