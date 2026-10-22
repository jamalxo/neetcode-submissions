class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        
        for i in range(n):
            adj_list.setdefault(i, [])

        for edge in edges:
            i,j = edge
            adj_list[i].append(j)
            adj_list[j].append(i)
        
        counter = 0

        self.visited = set()
        
        def dfs(node, prev):
            if node in self.visited:
                return
            self.visited.add(node)
            connections = adj_list[node]
            for c in connections:
                if c != prev:
                    dfs(c, node)

        for i in range(n):
            if i in self.visited:
                continue
            counter += 1
            dfs(i, None)
            print(self.visited)


        return counter