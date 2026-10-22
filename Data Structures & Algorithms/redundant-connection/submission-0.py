class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {}

        for i in range(1, len(edges)+1):
            adj_list.setdefault(i, [])

        for edge in edges:
            i,j = edge
            adj_list[i].append(j)
            adj_list[j].append(i)

        self.start = -1

        visited = set()
        cycle = set()

        def dfs(node, prev):
            if node in visited:
                self.start = node
                return True

            visited.add(node)
            for c in adj_list[node]:
                if c != prev:
                    if dfs(c, node):
                        if self.start != -1:
                            cycle.add(node)
                        if node == self.start:
                            self.start = -1
                        return True
            return False

        dfs(1, None)

        res = None
        print(cycle)

        for edge in edges[::-1]:
            i, j = edge
            if i in cycle and j in cycle:
                return [i,j]
        