class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        curr = set()
        i = 0
        while i < len(nums):
            if nums[i] not in curr and len(curr) != k:
                curr.add(nums[i])
            elif nums[i] not in curr:
                curr.remove(nums[i-k])
                curr.add(nums[i])
            else:
                return True
            i+=1

        return False