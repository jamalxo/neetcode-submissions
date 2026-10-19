class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []

        candidates = sorted(candidates)
        

        def dfs(i, curr, summed):
            
            if summed == target:
                self.res.append(curr.copy())
                return
            if summed > target or i == len(candidates):
                return

            #include
            curr.append(candidates[i])
            dfs(i+1, curr, summed + candidates[i])
            curr.pop()
            #skip
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr, summed)

        dfs(0, [], 0)

        return self.res