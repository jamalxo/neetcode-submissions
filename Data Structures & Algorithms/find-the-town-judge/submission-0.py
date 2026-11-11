class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {}

        for i in range(1,n+1):
            adj.setdefault(i, set())

        for i in range(len(trust)):
            one, two = trust[i]
            adj[one].add(two)

        potentials = []

        for k,v in adj.items():
            if not v:
                potentials.append(k)

        res = None

        for i in range(len(potentials)):
            yes = True
            for k,v in adj.items():
                if potentials[i] != k and potentials[i] not in v:
                    yes = False
            if yes:
                res = potentials[i]
        
        return res if res else -1

