class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        self.current_subset = []
        def dfs(i):
            if i >= len(nums):
                self.res.append(self.current_subset.copy())
                return

            self.current_subset.append(nums[i])
            dfs(i + 1)

            self.current_subset.pop()
            dfs(i + 1)

        dfs(0)

        print(self.res)

        return self.res