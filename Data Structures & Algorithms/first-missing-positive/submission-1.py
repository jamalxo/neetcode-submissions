class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()

        for i, n in enumerate(nums):
            seen.add(n)


        for i in range(1, 2**31):
            if i not in seen:
                return i       
