class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []


        def dfs(pm, existing):
            print(pm, existing)
            if len(pm) == len(nums):
                print("adding")
                self.res.append(pm.copy())
                return
            
            for i in range(len(nums)):
                if i in existing:
                    continue

                existing.add(i)
                pm.append(nums[i])
                dfs(pm, existing)
                pm.pop()
                existing.remove(i)



        dfs([], set())

        return self.res