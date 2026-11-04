class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums = sorted(nums)

        def dfs(i, arr):
            if i == len(nums):
                res.append(arr)
                return

            #take or skip
            new = arr + [nums[i]]
            dfs(i+1, new)
            print(res)

            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j+=1
            
            dfs(j, arr)
        

        dfs(0, [])

        return res