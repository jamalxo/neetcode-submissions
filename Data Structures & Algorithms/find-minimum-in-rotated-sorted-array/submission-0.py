class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        res = 0

        while nums[l] > nums[r]:
            middle = (l + r ) // 2

            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle

            if nums[l] < nums[r]:
                res = min(res, nums[l])
        return nums[l]