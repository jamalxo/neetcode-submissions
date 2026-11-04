class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        mapped = {}

        for i in range(len(nums)):
            mapped[nums[i]] = mapped.get(nums[i], 0) +1

        print(mapped)

        def dfs(arr):
            if len(arr) == len(nums):
                res.append(arr)
                return


            for k,v in mapped.items():
                if v != 0:
                    new = arr + [k]
                    mapped[k] -= 1
                    dfs(new)
                    mapped[k] += 1


        dfs([])
        print(res)
        return res