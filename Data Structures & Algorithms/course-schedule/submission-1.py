class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        c_p = {}
        in_degree_count = [0] * numCourses

        for i in range(0, numCourses):
            c_p.setdefault(i, []) 
    

        for course, pre in prerequisites:
            c_p[pre].append(course)
            in_degree_count[course] += 1
        
        print(c_p)
        print(in_degree_count)

        starting = []
        for i in range(len(in_degree_count)):
            if in_degree_count[i] == 0:
                starting.append(i)

        res = []
        def dfs(course):
            if in_degree_count[course] == 0:
                res.append(course)
                for unlocked in c_p[course]:
                    in_degree_count[unlocked] -= 1
                    if in_degree_count[unlocked] == 0:
                        dfs(unlocked)
        for s in starting:
            dfs(s)
        
        return len(res) == numCourses
            