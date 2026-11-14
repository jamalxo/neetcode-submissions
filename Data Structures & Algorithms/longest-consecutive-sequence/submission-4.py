class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setted = set(nums)

        if not nums:
            return 0

        res = 0

        for i in range(len(nums)):
            if nums[i] - 1 in setted:
                continue
            #streak this shit
            else:
                streak = 0
                val = nums[i]
                while val in setted:
                    streak += 1
                    val += 1
                res = max(streak, res)
        
        return res