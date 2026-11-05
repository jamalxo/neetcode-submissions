class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #divide = len(nums) / 3 
#
        #if not divide % 1 == 0:
        #    return False

        maxi = sum(nums) // k
        nums.sort(reverse=True)
        if sum(nums) / k % 1 != 0:
            return False

        mapped = {}

        for i in range(k):
            mapped[i] = 0

        cache = {}

        def dfs(i):
            if i == len(nums):
                return len(set(mapped.values())) == 1

            tried = set() 
            for k,v in mapped.items():
                if v in tried:  # already tried a bucket with this sum at this level
                    continue
                if mapped[k] + nums[i] > maxi:
                    continue
                tried.add(v)
                mapped[k] += nums[i]
                if dfs(i+1):
                    return True
                mapped[k] -= nums[i]
            
            return False

        test = dfs(0)
        return test

