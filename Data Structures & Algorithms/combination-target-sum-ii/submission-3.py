class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)


        def dfs(i, arr, total):
            if total > target:
                return
            if total == target:
                res.append(arr.copy())

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                appending = arr.copy()
                appending.append(candidates[j])
                dfs(j+1, appending, total+candidates[j])


        dfs(0, [], 0)

        return res