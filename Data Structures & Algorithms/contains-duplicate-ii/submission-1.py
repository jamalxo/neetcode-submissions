class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # find duplicate

        # and then are they at most this much apart

        # fixed sliding window k
        if k == 0:
            return False
        curr = set()
        i = 0
        while i < len(nums):
            if len(curr) != k:
                if nums[i] not in curr:
                    curr.add(nums[i])
                else:
                    return True
            else:
                if nums[i] not in curr:
                    curr.remove(nums[i-k])
                    curr.add(nums[i])
                else:
                    return True

            i+=1

        return False