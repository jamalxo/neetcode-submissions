class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        reach = {}

        for i in range(n):
            reach.setdefault(i, [])

        for edge in edges:
            i, j = edge
            reach[i].append(j)
            reach[j].append(i)

        visited = set()

        self.valid = True

        def dfs(node, prev):
            print("going to", node, " from ", prev)
            if node in visited:
                self.valid = False
                return
            visited.add(node)
            
            connections = reach[node]
            for c in connections:
                if c != prev:
                    dfs(c, node)
        print(reach)
        dfs(0, None)

        print(visited)

        return self.valid if len(visited) == n else False