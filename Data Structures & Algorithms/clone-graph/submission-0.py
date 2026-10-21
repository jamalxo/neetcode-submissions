"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        self.oldToNew = {}

        def dfs(node):
            if not node:
                return
            
            copy = Node(node.val)
            self.oldToNew[node] = copy
            for n in node.neighbors:
                if n not in self.oldToNew:
                    dfs(n)
        
        dfs(node)

        for old, new in self.oldToNew.items():
            adj = []
            for n in old.neighbors:
                
                adj.append(self.oldToNew[n])
            new.neighbors = adj

        return self.oldToNew[node]